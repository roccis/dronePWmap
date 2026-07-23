import streamlit as st

def page_links():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('dronePWmap_app.py', label='Home', icon='🏠')
        st.page_link('pages/1_dronepilotcert.py', label='Drone Pilot Certification', icon='👨‍✈️')
        st.page_link('pages/2_dronesoftwareselect.py', label='Drone Software Selection', icon='💻')
        st.page_link('pages/3_howtoguides.py', label='How-To Guides', icon='📖')
        st.page_link('pages/4_vinesizesensing.py', label='Vine Size Sensing for Crop Load Management', icon='🍇')
