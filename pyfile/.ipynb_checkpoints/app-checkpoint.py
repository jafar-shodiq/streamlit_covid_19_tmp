import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
satu dua tiga
""")
 
df = pd.read_csv("../data/children_thr_data.csv", sep=";")
st.line_chart(df)