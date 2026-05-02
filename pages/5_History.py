import streamlit as st
import pandas as pd

st.title("📁 Previous Records")

try:

    df = pd.read_csv("data/records.csv")

    st.dataframe(df)

except:
    
    st.info("No records found")