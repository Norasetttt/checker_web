import streamlit as st
import os
import pandas as pd



# Read the CSV file into a DataFrame
df = pd.read_csv("all_file.csv")


st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygULcmljayBhc3RsZXk%3Dl")
st.title("My Streamlit App")
st.write("Welcome to my first Streamlit app!")
st.dataframe(df)
if st.button("submit"):
    st.write('submitted')
