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


def create_pages(yid_list) :
    pages = {}
    yid_pages = [yid+'_page' for yid in yid_list]
    for yid in yid_list :
        for page in yid_pages:        
            def page () :
                indices = []
                for id in list(df["File Name"]) :
                    if id == yid :
                        indices.append(list(df["File Name"]).index(id))
                for i in range(min(indices),max(indices)+1) :
                    st.title("start time "+str(df["start_time"][i]))
                    if st.button("Jump to start"):
                        video = st.video("https://www.youtube.com/watch?v="+yid , start_time = convert_time_to_seconds(df["start_time"][i]))  
                    st.data_editor(get_row(df,i)) 
            pages[yid] = page
    return pages 



pages = create_pages(yid_list)

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()      



