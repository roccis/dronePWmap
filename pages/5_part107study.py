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
- [Regulations](#regulations)
- [Airspace classification, operating requirements, and flight restrictions](#airspace-classification)
- [Aviation weather](#aviation-weather)
- [Small unmanned aircraft loading](#aircraft-loading)
- [Emergency procedures](#emergency-procedures)
- [Crew resource management](#crew-resource-management)
- [Radio communication procedures](#radio-communication)
- [Aircraft performance](#aircraft-performance)
- [Physiological factors affecting pilot performance](#physiological-factors)
- [Aeronautical decision-making and judgment](#decision-making)
- [Airport operations](#airport-operations)
- [Maintenance and preflight inspection procedures](#maintenance-and-preflight)
"""
)

st.header("Regulations", anchor="regulations")
st.write("Review the Part 107 rules and operating limitations that apply to remote pilots.")

st.header("Airspace classification, operating requirements, and flight restrictions", anchor="airspace-classification")
st.write("Study airspace classes, how to determine authorization requirements, and where flight restrictions apply.")

st.header("Aviation weather", anchor="aviation-weather")
st.write("Review aviation weather reports, forecasts, and how weather conditions affect small unmanned aircraft.")

st.header("Small unmanned aircraft loading", anchor="aircraft-loading")
st.write("Understand how loading and weight affect an aircraft's balance and safe operation.")

st.header("Emergency procedures", anchor="emergency-procedures")
st.write("Study how to respond to abnormal situations and emergencies while maintaining control of the aircraft.")

st.header("Crew resource management", anchor="crew-resource-management")
st.write("Review effective communication, task management, and coordination with people supporting a flight.")

st.header("Radio communication procedures", anchor="radio-communication")
st.write("Learn the communication procedures and terminology relevant to small unmanned aircraft operations.")

st.header("Aircraft performance", anchor="aircraft-performance")
st.write("Review factors that affect small unmanned aircraft performance and how to make performance-related decisions.")

st.header("Physiological factors affecting pilot performance", anchor="physiological-factors")
st.write("Study how fatigue, stress, medication, alcohol, and other physiological factors can affect safe pilot performance.")

st.header("Aeronautical decision-making and judgment", anchor="decision-making")
st.write("Review risk assessment and sound aeronautical decision-making before and during a flight.")

st.header("Airport operations", anchor="airport-operations")
st.write("Study airport environments, traffic patterns, and safe operations near airports.")

st.header("Maintenance and preflight inspection procedures", anchor="maintenance-and-preflight")
st.write("Review aircraft maintenance responsibilities and the checks to complete before flight.")

st.page_link(
    "pages/1_dronepilotcert.py",
    label="← Back to Drone Pilot Certification",
    icon="👨‍✈️",
)
