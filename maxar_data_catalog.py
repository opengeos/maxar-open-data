import os
import glob
import geojson
import leafmap
import geopandas as gpd
import pandas as pd
from pystac import Catalog
from shapely.ops import unary_union

# stac-browser: https://bit.ly/3sTkrWm
url = "https://maxar-opendata.s3.amazonaws.com/events/catalog.json"
root_catalog = Catalog.from_file(url)
collections = root_catalog.get_collections()
collections = [collection.id for collection in collections]

datasets = pd.read_csv("datasets.csv")


def union_geojson_with_attributes(input_file):
    # Read the input GeoJSON file
    output_file = input_file.replace(".geojson", "_union.geojson")
    data = gpd.read_file(input_file)

    # Perform the union operation on all polygons
    union_polygon = unary_union(data["geometry"])

    # Create a new GeoDataFrame with the unioned geometry
    union_gdf = gpd.GeoDataFrame(geometry=[union_polygon])

    columns = data.columns.tolist()
    columns.remove("geometry")

    # Copy attributes from the first row of the input GeoDataFrame
    for column in columns:
        union_gdf[column] = data.iloc[0][column]

    # Save the GeoDataFrame with unioned geometry and attributes as a new GeoJSON file
    union_gdf.to_file(output_file, driver="GeoJSON")


for index, collection in enumerate(collections):
    print("*****************************************************************")
    print(f"Processing {index+1}/{len(collections)}: {collection} ...")

    # output = f"footprints/{collection}.geojson"
    # if not os.path.exists(output):
    #     gdf = leafmap.maxar_all_items(collection, verbose=False)
    #     gdf.to_file(output, driver="GeoJSON")

    out_dir = f"datasets/{collection}"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    cols = leafmap.maxar_child_collections(collection)
    if collection in datasets["dataset"].tolist():
        count = datasets[datasets["dataset"] == collection]["count"].item()
    else:
        count = 0

    # Generate individual GeoJSON files for each collection
    for i, col in enumerate(cols):
        print(f"Processing {i+1}/{len(cols)}: {col} ...")
        output = f"datasets/{collection}/{col}.geojson"
        if not os.path.exists(output):
            gdf = leafmap.maxar_items(
                collection,
                col,
                return_gdf=True,
                assets=["visual", "ms_analytic", "pan_analytic", "data-mask"],
            )
            gdf.to_file(output, driver="GeoJSON")
        union_geojson_with_attributes(output)

    # Merge all GeoJSON files into one GeoJSON file
    merged = f"datasets/{collection}.geojson"
    merged_union = f"datasets/{collection}_union.geojson"
    if os.path.exists(merged):
        gdf = gpd.read_file(merged)
    else:
        gdf = gpd.GeoDataFrame()

    files = leafmap.find_files(out_dir, ext="geojson")
    files = [file for file in files if "union" not in file]
    gdfs = [gpd.read_file(file) for file in files]
    merged_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True)).drop(
        ["proj:geometry"], axis=1
    )

    print(f"Total number of images before: {count}")
    print(f"Total number of images after: {len(merged_gdf)}")

    if len(gdf) != len(merged_gdf):
        merged_gdf.sort_values(by=["datetime", "quadkey"], ascending=True, inplace=True)
        merged_gdf.to_file(merged, driver="GeoJSON")

    files = leafmap.find_files(out_dir, ext="geojson")
    files = [file for file in files if "union" in file]
    gdfs = [gpd.read_file(file) for file in files]
    merged_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True)).drop(
        ["proj:geometry"], axis=1
    )
    merged_gdf.to_file(merged_union, driver="GeoJSON")

    # Create MosaicJSON for each tile
    files = leafmap.find_files(out_dir, ext="geojson")
    files = [file for file in files if "union" not in file]
    for file in files:
        out_json = file.replace(".geojson", ".json")
        if not os.path.exists(out_json):
            print(f"Processing {file} ...")
            gdf = gpd.read_file(file)
            images = gdf["visual"].tolist()
            leafmap.create_mosaicjson(images, out_json)

    # Create TSV file for each event
    files = leafmap.find_files("datasets", ext="geojson", recursive=False)
    files = [file for file in files if "union" not in file]
    for file in files:
        out_tsv = file.replace(".geojson", ".tsv")
        gdf = gpd.read_file(file)
        df = leafmap.gdf_to_df(gdf)
        df.sort_values(by=["datetime", "quadkey"], ascending=True, inplace=True)
        df.to_csv(out_tsv, sep="\t", index=False)

# Create a CSV file for all events
files = leafmap.find_files("datasets", ext="tsv", recursive=False)
ids = []
nums = []
for file in files:
    df = pd.read_csv(file, sep="\t")
    ids.append(file.split("/")[1].replace(".tsv", ""))
    nums.append(len(df))
df = pd.DataFrame({"dataset": ids, "count": nums})
df.sort_values(by=["dataset"], ascending=True, inplace=True)
df.to_csv("datasets.csv", index=False)
