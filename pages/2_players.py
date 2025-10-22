import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃",
    layout="wide"
)

df_data = st.session_state["data"]
df_data