import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

url = 'https://giswqs.github.io/maxar-open-data'
repo = 'https://github.com/giswqs/maxar-open-data/blob/master/datasets'
m = leafmap.Map()


@st.cache
def get_datasets():
    datasets = f'{url}/datasets.csv'
    df = pd.read_csv(datasets)
    return df


@st.cache
def get_catalogs(name):
    dataset = f'{url}/datasets/{name}.tsv'

    dataset_df = pd.read_csv(dataset, sep='\t')
    catalog_ids = dataset_df['catalog_id'].unique().tolist()
    return catalog_ids


st.title('Visualizing Maxar Open Data')

col1, col2 = st.columns([1.2, 3.8])

with col1:
    default = 'Kahramanmaras-turkey-earthquake-23'
    datasets = get_datasets()['dataset'].tolist()
    dataset = st.selectbox('Select a dataset', datasets, index=datasets.index(default))
    catalog = st.selectbox('Select a COG mosaic', get_catalogs(dataset))
    geojson = f'{url}/datasets/{dataset}.geojson'
    mosaic = f'{url}/datasets/{dataset}/{catalog}.json'
    tsv = f'{repo}/{dataset}/{catalog}.tsv'
    st.markdown(f'View metadata: [{catalog}.tsv]({tsv})')

    with st.expander("Python code snippets"):
        markdown = f"""
import leafmap.foliumap as leafmap
m = leafmap.Map()
geojson = '{geojson}'
mosaic = '{mosaic}'
m.add_geojson(geojson, layer_name='{dataset}', info_mode='on_click')
m.add_stac_layer(mosaic, name='{catalog}')
m
        """
        st.code(markdown)


    style = {
        'weight': 1,
        'fillOpacity': 0
    }
    m.add_geojson(geojson, layer_name=dataset, style=style, info_mode='on_click')
    m.add_stac_layer(mosaic, name=catalog)

    st.info('About')
    markdown = f"""
    - [Web App Source Code](https://github.com/giswqs/maxar-open-data/blob/master/streamlit_app.py)
    - [GitHub Repo](https://github.com/giswqs/maxar-open-data)
    - [Notebook Example](https://github.com/giswqs/maxar-open-data/blob/master/examples/maxar_open_data.ipynb)
    - [Maxar Open Data Program](https://www.maxar.com/open-data)
    - [Maxar Open Data on AWS](https://registry.opendata.aws/maxar-open-data/)
    - [Maxar Open Data on STAC Index](https://stacindex.org/catalogs/maxar-open-data-catalog-ard-format#/)
    - [Maxar Open Data on STAC Browser](https://radiantearth.github.io/stac-browser/#/external/maxar-opendata.s3.amazonaws.com/events/catalog.json?.language=en)
    - Contact: [Qiusheng Wu](https://github.com/giswqs)
    """
    st.markdown(markdown)

with col2:
    m.to_streamlit(height=780)
