import streamlit as st
import pandas as pd


df = pd.read_csv("multipage/all_file.csv")
new_df = df.set_index('start_time')

yid_list = [df["File Name"][0]]
for i in range(1, len(df["File Name"])):
    if df["File Name"][i - 1] != df["File Name"][i]:
        yid_list.append(df["File Name"][i].strip())

def convert_time_to_seconds(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

def get_row(df,row):
    return df.iloc[row,0:2]

def page1() :
    st.title("Page1!!!")
    


page = st.sidebar.radio("page1")
page()


st.title("Please recheck for me")
st.write("URL = https://www.youtube.com/watch?v="+yid_list[0])
if st.button("Jump to start",help = '??'): #add help() and function below worked somehow
    st.video("https://www.youtube.com/"+yid_list[0], start_time = convert_time_to_seconds(df["start_time"][1]))
st.experimental_data_editor(get_row(df,0))




