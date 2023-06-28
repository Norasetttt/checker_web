import streamlit as st
import os
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account


# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\47gia\Downloads\all_file.csv')
scrollable_content  = '<div style="height: 10px; overflow: scroll;">'+df['answer'][0]+ '</div>' 
df.at[0, 'answer'] = scrollable_content

st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygULcmljayBhc3RsZXk%3Dl")
st.title("My Streamlit App")
st.write("Welcome to my first Streamlit app!")
st.table(df)
if st.button("submit"):
    st.write('submitted')
