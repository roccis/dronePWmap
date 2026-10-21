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
- [Airspace Classification, Operating Requirements, and Flight Restricitons](#airspace-classification)
- [Aviation Weather Sources and Effects of Weather on Small Unmanned Aircraft Performance](#aviation-weather)
- [Small Unmanned Aircraft Loading](#aircraft-loading)
- [Emergency Procedures](#emergency-procedures)
- [Crew Resource Management](#crew-resource-management)
- [Radio Communication Procedures](#radio-communication)
- [Determining the Performance of Small Unmanned Aircraft](#aircraft-performance)
- [Physiological Factors (Including Drugs and Alcohol) Affecting Pilot Performance](#physiological-factors)
- [Aeronautical Decision-Making and Judgment](#decision-making)
- [Airport Operations](#airport-operations)
- [Maintenance and Preflight Inspection Procedures](#maintenance-and-preflight)
"""
)

st.header("Regulations", anchor="regulations")
st.write("You should be familiar with applicable regulations mentioned in the [Code of Federal Regulations Title 14 Part 107](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107),\n"
         "as well as [FAA Advisory Circular 107-2](http://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_107-2.pdf). These might be a bit tedious to read through and they are more or less covered below.")

st.header("Airspace Classification, Operating Requirements, and Flight Restricitons", anchor="airspace-classification")
st.write("Ideally, NY State growers will be flying in uncontrolled Class G airspace, but you should be familiar with the different \n"
        "airspace classes and their operating requirements and restrictions. Regardless you will need to know how to read sectional \n"
        "charts and understand the different airspace classes, their operating requirements, and flight restrictions.")

st.header("Aviation Weather Sources and Effects of Weather on Small Unmanned Aircraft Performance", anchor="aviation-weather")
st.write("Review aviation weather reports, forecasts, and how weather conditions affect small unmanned aircraft.")

st.header("Small Unmanned Aircraft Loading", anchor="aircraft-loading")
st.write("Understand how loading and weight affect an aircraft's balance and safe operation.")

st.header("Emergency Procedures", anchor="emergency-procedures")
st.write("Study how to respond to abnormal situations and emergencies while maintaining control of the aircraft.")

st.header("Crew Resource Management", anchor="crew-resource-management")
st.write("Review effective communication, task management, and coordination with people supporting a flight.")

st.header("Radio Communication Procedures", anchor="radio-communication")
st.write("Learn the communication procedures and terminology relevant to small unmanned aircraft operations.")

st.header("Determining the Performance of Small Unmanned Aircraft", anchor="aircraft-performance")
st.write("Review factors that affect small unmanned aircraft performance and how to make performance-related decisions.")

st.header("Physiological Factors (Including Drugs and Alcohol) Affecting Pilot Performance", anchor="physiological-factors")
st.write("Study how fatigue, stress, medication, alcohol, and other physiological factors can affect safe pilot performance.")

st.header("Aeronautical Decision-Making and Judgment", anchor="decision-making")
st.write("Review risk assessment and sound aeronautical decision-making before and during a flight.")

st.header("Airport Operations", anchor="airport-operations")
st.write("Study airport environments, traffic patterns, and safe operations near airports.")

st.header("Maintenance and Preflight Inspection Procedures", anchor="maintenance-and-preflight")
st.write("Review aircraft maintenance responsibilities and the checks to complete before flight.")

st.page_link(
    "pages/1_dronepilotcert.py",
    label="← Back to Drone Pilot Certification",
    icon="👨‍✈️",
)
