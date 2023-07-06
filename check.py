import streamlit as st
import pandas as pd
df = pd.read_csv(r"C:\Users\47gia\Downloads\create_web\all_file.csv")

yid_list = [df["File Name"][0]]
for i in range(1, len(df["File Name"])):
    if df["File Name"][i - 1] != df["File Name"][i]:
        yid_list.append(df["File Name"][i])



# create page's appearance // i = index of interest row
def create_page(i):
    def page():
        st.title(str(df["start_time"][i]) + '  to  ' + str(df["end_time"][i]))
        st.text_input("question", value=str(df["question"][i]))
        st.text_input("answer", value=str(df["answer"][i]))
    return page

# create a multiple pages with list of youtube-id /// return a dictionary with youtube-id as a key and function that contain details of each youtube-id as a value 
def create_pages(yid_list):
    pages = {}
    yid_pages = [yid for yid in yid_list]
    # create dict of pages {page name : function} (function containing page's details)
    for yid, page_key in zip(yid_list, yid_pages):
        # create one page
        # get row and column of youtube_id's q&a from dataframe
        indices = []
        for i, id in enumerate(list(df["File Name"])):
            if id == yid:
                indices.append(i)
        pages[page_key] = []
        for i in range(min(indices), max(indices) + 1):
            pages[page_key].append(create_page(i))
    return pages


print(create_pages(yid_list))