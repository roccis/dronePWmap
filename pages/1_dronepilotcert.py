import streamlit as st
from pathlib import Path
import functions

st.set_page_config(layout="wide")

st.title("Drone Pilot Certification")

functions.page_links()

st.header(
    "[Steps to becoming a Certified Remote Pilot](https://www.faa.gov/uas/commercial_operators) for commercial operations are "
    "provided by the Federal Aviation Administraion (FAA). The goal of this module is to provide a simplified overview "
    "intended specifically for interested vineyard operators in New York State."
)
st.subheader("First, why do you need to be certified?")
st.write(
    "As a vineyard owner or employee operating a drone for commercial purposes, "
    " you are required to operate under Part 107 rules."
    )