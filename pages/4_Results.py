import streamlit as st
import pandas as pd
from datetime import datetime
import os


st.title("📊 Results")


# check if user profile exists
if "user" not in st.session_state:

    st.warning("⚠ Please fill User Profile first")

    st.switch_page("pages/2_User_Profile.py")


# retrieve values
bpm = st.session_state.get("bpm", 0)
rr = st.session_state.get("rr", 0)


# display user info
user = st.session_state["user"]

st.subheader("User Details")

col1, col2, col3 = st.columns(3)

col1.write(f"Name: {user['name']}")
col2.write(f"Age: {user['age']}")
col3.write(f"Gender: {user['gender']}")


st.markdown("---")


# show results

col1, col2 = st.columns(2)

col1.metric("❤️ Heart Rate", f"{bpm} BPM")
col2.metric("🫁 Breathing Rate", f"{rr} /min")


signal = st.session_state.get("signal", [])

st.line_chart(signal)


# health status

if 60 <= bpm <= 100:
    st.success("Heart Rate is Normal")
else:
    st.warning("Heart Rate outside normal range")


# save record

record = {

"name": user["name"],
"age": user["age"],
"gender": user["gender"],
"user_id": user["id"],

"heart_rate": bpm,
"breathing_rate": rr,

"date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

}


file_path = "data/records.csv"


df = pd.DataFrame([record])


if os.path.exists(file_path):

    df.to_csv(file_path, mode="a", header=False, index=False)

else:

    df.to_csv(file_path, index=False)


st.success("Result saved successfully")