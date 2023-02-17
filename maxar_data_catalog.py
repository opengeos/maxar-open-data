import os
import glob
import geojson
import leafmap
import geopandas as gpd
import pandas as pd

collections = leafmap.maxar_collections()

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

    for i, col in enumerate(cols):
        print(f"Processing {i+1}/{len(cols)}: {col} ...")
        output = f"datasets/{collection}/{col}.geojson"
        if not os.path.exists(output):
            gdf = leafmap.maxar_items(collection, col, return_gdf=True, assets=['visual'])
            gdf.to_file(output, driver="GeoJSON")
                                  

    files = leafmap.find_files(out_dir)
    gdfs = [gpd.read_file(file) for file in files]
    merged_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True)) 
    merged_gdf.to_file(f"datasets/{collection}.geojson", driver="GeoJSON")