import streamlit as st
import os
import pandas as pd


df = pd.read_csv("all_file.csv")


def df_to_table() :
    
    return

st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygULcmljayBhc3RsZXk%3Dl")
st.title("My Streamlit App")
st.write("Welcome to my first Streamlit app!")
st.experimental_data_editor(df)
if st.button("submit"):
    st.write('submitted')
