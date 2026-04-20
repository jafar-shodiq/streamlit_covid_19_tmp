import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
satu dua tiga
""")
 
df = pd.read_csv("streamlit/children_thr_data.csv")
df["age"] = df["age"].astype(int)
st.line_chart(data=df, x="name", y="age")