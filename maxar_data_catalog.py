import leafmap

collections = leafmap.maxar_collections()

for index, collection in enumerate(collections):
    print(f"Processing {index+1}/{len(collections)}: {collection} ...")

    gdf = leafmap.maxar_all_items(collection, verbose=False)
    gdf.to_file(f"footprints/{collection}.geojson", driver="GeoJSON")