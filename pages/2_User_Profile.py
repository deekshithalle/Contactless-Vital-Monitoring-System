import streamlit as st

st.title("👤 User Profile")

name = st.text_input("Full Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    step=1
)

gender = st.selectbox(
    "Gender",
    ["Male","Female","Other"]
)

user_id = st.text_input("User ID")

if st.button("Continue"):

    if name == "" or user_id == "":
        st.warning("Please fill all details")

    else:

        st.session_state["user"] = {

            "name": name,
            "age": age,
            "gender": gender,
            "id": user_id

        }

        st.success("Profile saved")

        st.switch_page("pages/3_Capture_Analysis.py")