import os
import glob
import geojson
import leafmap
import geopandas as gpd
import pandas as pd
from pystac import Catalog

url = "https://maxar-opendata.s3.amazonaws.com/events/catalog.json"
root_catalog = Catalog.from_file(url)
collections = root_catalog.get_collections()
collections = [collection.id for collection in collections]

datasets = pd.read_csv('datasets.csv')

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
    count = datasets[datasets['dataset'] == collection]['count'].item()

    # Generate individual GeoJSON files for each collection
    for i, col in enumerate(cols):
        print(f"Processing {i+1}/{len(cols)}: {col} ...")
        output = f"datasets/{collection}/{col}.geojson"
        if not os.path.exists(output):
            gdf = leafmap.maxar_items(
                collection, col, return_gdf=True, assets=['visual']
            )
            gdf.to_file(output, driver="GeoJSON")

    # Merge all GeoJSON files into one GeoJSON file
    merged = f"datasets/{collection}.geojson"
    gdf = gpd.read_file(merged)

    files = leafmap.find_files(out_dir, ext='geojson')
    gdfs = [gpd.read_file(file) for file in files]
    merged_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True)).drop(
        ['proj:geometry'], axis=1
    )
    
    print(f"Total number of images before: {count}")
    print(f"Total number of images after: {len(merged_gdf)}")

    if len(gdf) != len(merged_gdf):
        merged_gdf.sort_values(by=['datetime', 'quadkey'], ascending=True, inplace=True)
        merged_gdf.to_file(merged, driver="GeoJSON")

    # Create MosaicJSON for each tile
    files = leafmap.find_files(out_dir, ext='geojson')
    for file in files:
        out_json = file.replace('.geojson', '.json')
        if not os.path.exists(out_json):
            print(f"Processing {file} ...")
            gdf = gpd.read_file(file)
            images = gdf['visual'].tolist()
            leafmap.create_mosaicjson(images, out_json)

    # Create TSV file for each event
    files = leafmap.find_files('datasets', ext='geojson')
    for file in files:
        out_tsv = file.replace('.geojson', '.tsv')
        gdf = gpd.read_file(file)
        df = leafmap.gdf_to_df(gdf)
        df.sort_values(by=['datetime', 'quadkey'], ascending=True, inplace=True)
        df.to_csv(out_tsv, sep='\t', index=False)

# Create a CSV file for all events
files = leafmap.find_files('datasets', ext='tsv', recursive=False)
ids = []
nums = []
for file in files:
    df = pd.read_csv(file, sep='\t')
    ids.append(file.split('/')[1].replace('.tsv', ''))
    nums.append(len(df))
df = pd.DataFrame({'dataset': ids, 'count': nums})
df.sort_values(by=['dataset'], ascending=True, inplace=True)
df.to_csv('datasets.csv', index=False)
