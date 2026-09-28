import streamlit as st
from pathlib import Path
import functions

st.set_page_config(layout="wide")

st.title("Drone Pilot Certification")

functions.page_links()

st.write(
    "[Steps to becoming a Certified Remote Pilot](https://www.faa.gov/uas/commercial_operators) for commercial operations are "
    "provided by the Federal Aviation Administraion (FAA). "
)