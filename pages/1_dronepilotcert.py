import streamlit as st
from pathlib import Path
import functions

st.set_page_config(layout="wide")

st.title("Drone Pilot Certification")

functions.page_links()

st.header("Contents")
st.markdown("""
- [Overview](#overview)
- [Eligibility](#eligibility)
- [Create an FAA account](#create-an-faa-account)
- [Study for the knowledge test](#study-for-the-knowledge-test)
- [Take the knowledge test](#take-the-knowledge-test)
- [Apply for the certificate](#apply-for-the-certificate)
- [After certification](#after-certification)
- [Official resources](#official-resources)
""")

st.header("Overview", anchor="overview")
# Add section content here

st.subheader(
    "[Steps to becoming a Certified Remote Pilot](https://www.faa.gov/uas/commercial_operators) for commercial operations are "
    "provided by the Federal Aviation Administraion (FAA). The goal of this module is to provide a simplified overview "
    "intended specifically for interested vineyard operators in New York State."
)
st.subheader("First, why do you need to be certified?")
st.write(
    "As a vineyard owner or employee operating a drone for commercial purposes, "
    " you are required to operate under Part 107 rules."
    )
st.subheader("What is Part 107?")
st.write(
    "Part 107 is the set of rules and regulations that govern the operation of small unmanned aircraft systems (sUAS) for commercial purposes in the United States. "
    "It covers various aspects of drone operation, including pilot certification, operational limitations, and safety requirements. "
    "To legally operate a drone for commercial purposes, you must obtain a Remote Pilot Certificate from the Federal Aviation Administration (FAA) by passing the Part 107 Aeronautical Knowledge Test."
    )

st.header("Eligibility", anchor="eligibility")
# Add section content here

