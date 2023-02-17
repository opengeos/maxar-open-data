# maxar-open-data

## Introduction

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/maxar-open-data/blob/master/examples/turkey_earthquake.ipynb)
[![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/giswqs/maxar-open-data/blob/master/examples/turkey_earthquake.ipynb)

The [Maxar Open Data Program](https://www.maxar.com/open-data) provides pre- and post-event high-resolution satellite imagery in support of emergency planning, risk assessment, monitoring of staging areas and emergency response, damage assessment, and recovery. Check out the links below for more information.

- [Maxar Open Data Program](https://www.maxar.com/open-data)
- [Maxar Open Data on AWS](https://registry.opendata.aws/maxar-open-data/)
- [Maxar Open Data on STAC Index](https://stacindex.org/catalogs/maxar-open-data-catalog-ard-format#/)
- [Maxar Open Data on STAC Browser](https://radiantearth.github.io/stac-browser/#/external/maxar-opendata.s3.amazonaws.com/events/catalog.json?.language=en)

The Maxar Open Data STAC catalog URL is: https://maxar-opendata.s3.amazonaws.com/events/catalog.json. The repo contains the catalog in various formats, including GeoJSON, CSV, and MosaicJSON. This makes it easier to use the datasets with Python and other programming languages.

## Examples

### Visualizing image footprints

```python
import leafmap
m = leafmap.Map(center=[36.844461, 37.386475], zoom=8)
url = 'https://github.com/giswqs/maxar-open-data/raw/master/datasets/Kahramanmaras-turkey-earthquake-23.geojson'
m.add_geojson(url, layer_name="Footprints")
m
```

![](https://i.imgur.com/MesGklq.gif)

### Visualizing COG mosaic

```python
m = leafmap.Map()
url = 'https://giswqs.github.io/maxar-open-data/datasets/Kahramanmaras-turkey-earthquake-23/1050050044DE7E00.json'
m.add_stac_layer(url, name="Mosaic")
m
```

![](https://i.imgur.com/AaglnPQ.gif)

## Relevant Projects

- A list of open datasets on AWS: [aws-open-data](https://github.com/giswqs/aws-open-data)
- A list of open geospatial datasets on AWS: [aws-open-data-geo](https://github.com/giswqs/aws-open-data-geo)
- A list of open geospatial datasets on AWS with a STAC endpoint: [aws-open-data-stac](https://github.com/giswqs/aws-open-data-stac)
- A list of STAC endpoints from stacindex.org: [stac-index-catalogs](https://github.com/giswqs/stac-index-catalogs)
- A list of geospatial datasets on Microsoft Planetary Computer: [Planetary-Computer-Catalog](https://github.com/giswqs/Planetary-Computer-Catalog)
- A list of geospatial datasets on Google Earth Engine: [Earth-Engine-Catalog](https://github.com/giswqs/Earth-Engine-Catalog)
- A list of geospatial datasets on NASA's Common Metadata Repository (CMR): [NASA-CMR-STAC](https://github.com/giswqs/NASA-CMR-STAC)
- A list of geospatial data catalogs: [geospatial-data-catalogs](https://github.com/giswqs/geospatial-data-catalogs)
- The Maxar Open Data STAC Catalog: [maxar-open-data](https://github.com/giswqs/maxar-open-data)
