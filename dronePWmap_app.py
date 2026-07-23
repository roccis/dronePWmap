import streamlit as st
from pathlib import Path
import s3fs
import boto3

# Streamlit App
st.set_page_config(page_title="Drone training modules for NYS growers", layout="wide")

# Hardcoded Mapbox token
MAPBOX_TOKEN = st.secrets["mapbox"]["token"]

# AWS
s3_client = boto3.client('s3',aws_access_key_id = st.secrets["aws"]["access_key"], aws_secret_access_key = st.secrets["aws"]["secret_key"],region_name = st.secrets["aws"]["region"])
fs = s3fs.S3FileSystem(key=st.secrets["aws"]["access_key"], secret=st.secrets["aws"]["secret_key"])
bucket_name = st.secrets["aws"]["bucket_name"]
p = 'images'

st.title("Drone Training Modules for New York State Growers")
st.markdown("& Vineyard Pruning Weight Case Study")

def page_links():
    # builds the sidebar menu
    st.page_link('dronePWmap_app.py', label='Home', icon='🏠')
    st.page_link('pages/1_dronepilotcert.py', label='Drone Pilot Certification', icon='👨‍✈️')
    st.page_link('pages/2_dronesoftwareselect.py', label='Drone Software Selection', icon='💻')
    st.page_link('pages/3_howtoguides.py', label='How-To Guides', icon='📖')
    st.page_link('pages/4_vinesizesensing.py', label='Vine Size Sensing for Crop Load Management', icon='🍇')

page_links()