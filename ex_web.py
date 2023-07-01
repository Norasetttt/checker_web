import streamlit as st
import pandas as pd


df = pd.read_csv("all_file.csv")
new_df = df.set_index('start_time')


#create list of youtube id               
yid_list = [df["File Name"][0]]
for i in range(1, len(df["File Name"])):
    if df["File Name"][i - 1] != df["File Name"][i]:
        yid_list.append(df["File Name"][i])

def convert_time_to_seconds(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

def get_row(df,row):
    return df.iloc[row,0:2]

def get_unique_keys(number) :
    keys = []
    for i in range(number) :
        random_number = random.randint(1,50000)
        if random_number not in keys :
            keys.append(random_number)
    return keys 

def create_pages(yid_list):
    pages = {}
    yid_pages = [yid + '_page' for yid in yid_list]
    keys = get_unique_keys(1000)
    for yid, page_key in zip(yid_list, yid_pages):
        def create_page(yid_value):
            def page():
                indices = []
                for i, id in enumerate(list(df["File Name"])):
                    if id == yid_value:
                        indices.append(i)
                for i in range(min(indices), max(indices) + 1):
                    random_key = random.choice(keys)
                    st.title("start time " + str(df["start_time"][i]))
                    if st.button("Jump to start",key = random_key ):
                        video = st.video("https://www.youtube.com/watch?v=" + yid_value, start_time=convert_time_to_seconds(df["start_time"][i]))
                    st.data_editor(get_row(df, i))
                    keys.remove(random_key)
            return page

        pages[page_key] = create_page(yid)

    return pages



def main():
    pages = create_pages(yid_list)
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()      
