import streamlit as st
import pandas as pd
import random

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

#collect only interested row with question or answer columns
def get_row(df,row,column):###column 0 = question , colummn 1 = answer
    return df.iloc[row,column]

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
    yid_pages = [yid for yid in yid_list] #change to youtube name

    #create dict of pages {page name : function} (function contain page's details)
    for yid, page_key in zip(yid_list, yid_pages):
        #create one page
        def create_page(i):
            def page():
                st.title(str(df["start_time"][i]) + '  to  ' + str(df["end_time"][i]))
                st.text_input("question",value = str(df["question"][i]))
                st.text_input("answer",value = str(df["answer"][i]))
            return page()
            
            #get row and column of youtube_id's q&a from dataframe
        indices = [] 
        for i, id in enumerate(list(df["File Name"])):
            if id == yid:
                indices.append(i)
        pages[page_key] = []
        for i in range(min(indices),max(indices)+1) :
            pages[page_key].append(create_page(i))

    return pages


#start to build a web with csv dataframe
def main():
    pages = create_pages(yid_list)
    print(pages)
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection][0]
    page()
    

if __name__ == "__main__":
    main()      


