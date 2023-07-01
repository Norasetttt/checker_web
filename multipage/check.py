import streamlit as st
import pandas as pd
import os

df = pd.read_csv(r"C:\Users\47gia\Downloads\create_web\multipage\all_file.csv")

#create list of youtube id               
yid_list = [df["File Name"][0]]
for i in range(1, len(df["File Name"])):
    if df["File Name"][i - 1] != df["File Name"][i]:
        yid_list.append(df["File Name"][i])


for file in os.listdir(r"C:\Users\47gia\Downloads\create_web") :
    if file[0:9] == "multipage" and file[-3:] == ".py"  :
        os.remove(r"C:\Users\47gia\Downloads\create_web\\"+file)
print('finish')       