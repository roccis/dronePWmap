import streamlit as st
import functions

st.set_page_config(page_title="Part 107 Study Materials", layout="wide")

st.title("Part 107 Study Materials")
functions.page_links()

st.write(
    "Use these materials to prepare for the FAA Aeronautical Knowledge Test "
    "for Remote Pilots. Start with the official FAA study guide, then review "
    "each topic listed below."
)

st.link_button(
    "Open the FAA Remote Pilot Study Guide (PDF)",
    "https://www.faa.gov/sites/faa.gov/files/uas/resources/policy_library/remote_pilot_study_guide.pdf",
)

st.header("Knowledge test topics")
st.markdown(
    """
- Regulations
- Airspace classification, operating requirements, and flight restrictions
- Aviation weather sources and effects of weather on small unmanned aircraft performance
- Small unmanned aircraft loading
- Emergency procedures
- Crew resource management
- Radio communication procedures
- Determining the performance of small unmanned aircraft
- Physiological factors, including drugs and alcohol, affecting pilot performance
- Aeronautical decision-making and judgment
- Airport operations
- Maintenance and preflight inspection procedures
"""
)

st.page_link(
    "pages/1_dronepilotcert.py",
    label="← Back to Drone Pilot Certification",
    icon="👨‍✈️",
)
