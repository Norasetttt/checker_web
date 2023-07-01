import streamlit as st
import pandas as pd
import random
import deta

df = pd.read_csv("all_file.csv")

#create list of youtube id               
yid_list = [df["File Name"][0]]
for i in range(1, len(df["File Name"])):
    if df["File Name"][i - 1] != df["File Name"][i]:
        yid_list.append(df["File Name"][i])

#create time converter to use with video timestamp function 
def convert_time_to_seconds(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

#collect only interested row with question and answer columns
def get_row(df,row):
    return df.iloc[row,0:2]

#get a random number for a key to add in button function 
def get_unique_keys(number) :
    keys = []
    for i in range(number) :
        random_number = random.randint(1,50000)
        if random_number not in keys :
            keys.append(random_number)
    return keys 

# create a mutiple pages with list of youtube-id /// return a dictionary with youtube-id as a key and function that contain detail of each youtube-id as a value 
def create_pages(yid_list):
    pages = {}
    yid_pages = [yid + '_page' for yid in yid_list]
    keys = get_unique_keys(1000)
    for yid, page_key in zip(yid_list, yid_pages):
        def create_page(yid_value):
            def page():
                indices = []
                st.video("https://www.youtube.com/watch?v=" + yid_value)
                
                for i, id in enumerate(list(df["File Name"])):
                    if id == yid_value:
                        indices.append(i)
                
                for i in range(min(indices), max(indices) + 1):
                    random_key = random.choice(keys)
                    st.title("start time " + str(df["start_time"][i]))
                    st.data_editor(get_row(df, i))
                    keys.remove(random_key)
            return page

        pages[page_key] = create_page(yid)

    return pages


#start  \to build a web with csv dataframe
def main():
    pages = create_pages(yid_list)
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()      
