# maxar-open-data

## Introduction

[![image](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/opengeos/maxar-open-data/blob/master/examples/turkey_earthquake.ipynb)
[![image](https://img.shields.io/badge/Open-Planetary%20Computer-black?style=flat&logo=microsoft)](https://pccompute.westeurope.cloudapp.azure.com/compute/hub/user-redirect/git-pull?repo=https://github.com/opengeos/maxar-open-data&urlpath=lab/tree/maxar-open-data/examples/turkey_earthquake&branch=master)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/opengeos/maxar-open-data/blob/master/examples/turkey_earthquake.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/opengeos/maxar-open-data/master?urlpath=lab%2Ftree%2Fexamples)
[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/giswqs/solara-maxar)

The [Maxar Open Data Program](https://www.maxar.com/open-data) provides pre- and post-event high-resolution satellite imagery in support of emergency planning, risk assessment, monitoring of staging areas and emergency response, damage assessment, and recovery. Check out the links below for more information.

- [Maxar Open Data Program](https://www.maxar.com/open-data)
- [Maxar Open Data on AWS](https://registry.opendata.aws/maxar-open-data/)
- [Maxar Open Data on STAC Index](https://stacindex.org/catalogs/maxar-open-data-catalog-ard-format#/)
- [Maxar Open Data on STAC Browser](https://radiantearth.github.io/stac-browser/#/external/maxar-opendata.s3.amazonaws.com/events/catalog.json?.language=en)
- [Maxar Open Data on Hugging Face](https://huggingface.co/spaces/giswqs/solara-maxar)

The Maxar Open Data STAC catalog URL is: https://maxar-opendata.s3.amazonaws.com/events/catalog.json. The repo contains the catalog in various formats, including GeoJSON, CSV, and MosaicJSON. This makes it easier to use the datasets with Python and other programming languages.

## Examples

### Visualizing image footprints

```python
import leafmap
m = leafmap.Map(center=[36.844461, 37.386475], zoom=8)
url = 'https://github.com/opengeos/maxar-open-data/raw/master/datasets/Kahramanmaras-turkey-earthquake-23.geojson'
m.add_geojson(url, layer_name="Footprints")
m
```

![](https://i.imgur.com/MesGklq.gif)

### Visualizing COG mosaic

```python
m = leafmap.Map()
url = 'https://open.gishub.org/maxar-open-data/datasets/Kahramanmaras-turkey-earthquake-23/1050050044DE7E00.json'
m.add_stac_layer(url, name="Mosaic")
m
```

![](https://i.imgur.com/AaglnPQ.gif)

## Relevant Projects

- A list of open datasets on AWS: [aws-open-data](https://github.com/opengeos/aws-open-data)
- A list of open geospatial datasets on AWS: [aws-open-data-geo](https://github.com/opengeos/aws-open-data-geo)
- A list of open geospatial datasets on AWS with a STAC endpoint: [aws-open-data-stac](https://github.com/opengeos/aws-open-data-stac)
- A list of STAC endpoints from stacindex.org: [stac-index-catalogs](https://github.com/opengeos/stac-index-catalogs)
- A list of geospatial datasets on Microsoft Planetary Computer: [Planetary-Computer-Catalog](https://github.com/opengeos/Planetary-Computer-Catalog)
- A list of geospatial datasets on Google Earth Engine: [Earth-Engine-Catalog](https://github.com/opengeos/Earth-Engine-Catalog)
- A list of geospatial datasets on NASA's Common Metadata Repository (CMR): [NASA-CMR-STAC](https://github.com/opengeos/NASA-CMR-STAC)
- A list of geospatial data catalogs: [geospatial-data-catalogs](https://github.com/opengeos/geospatial-data-catalogs)
- The Maxar Open Data STAC Catalog: [maxar-open-data](https://github.com/opengeos/maxar-open-data)
- A Solara web app for visualizing Maxar Open Data: [solara-maxar](https://github.com/opengeos/solara-maxar)

## Demo

[![demo](https://img.youtube.com/vi/RBjZ5Ju09iU/0.jpg)](https://www.youtube.com/watch?v=RBjZ5Ju09iU)

## Tutorial

[![tutorial](https://img.youtube.com/vi/8t5M-EGR0sA/0.jpg)](https://www.youtube.com/watch?v=8t5M-EGR0sA)
