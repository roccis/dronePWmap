import streamlit as st
from pathlib import Path
import functions

st.set_page_config(layout="wide")

st.title("How-To Guides")

functions.page_links()