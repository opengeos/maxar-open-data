import os
import leafmap

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
                                  