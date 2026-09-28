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

st.subheader(
    "To be eligible for the Remote Pilot Certificate, you must meet the following requirements:"
    )
st.write(
    "- Be at least 16 years old\n"
    "- Be able to read, write, speak, and understand English\n"
    "- Be in a physical and mental condition to safely operate a drone\n"
    "- Pass the FAA's Aeronautical Knowledge Test (Part 107 test)\n"
    )

st.header("Create an FAA account", anchor="create-an-faa-account")
st.subheader(
    "You need to create an [Integrated Airman Certification and Rating Application (IACRA)](https://iacra.faa.gov/IACRA/Default.aspx) "
    "profile prior to registering for the knowledge test."
    )
st.write(
    "IACRA is the web-based certification/rating application that guides "
    "the user through the FAA's airman application process. IACRA helps ensure applicants meet regulatory and policy requirements "
    "through the use of extensive data validation. It also uses electronic signatures to protect the information's integrity, "
    "eliminates paper forms, and prints temporary certificates. Follow these steps:"
    )

