import streamlit as st

def on_upper_clicked():
    st.session_state.text = st.session_state.text.upper()

st.text_area("Enter text", key="text")
st.button("Upper Text", on_click=on_upper_clicked)