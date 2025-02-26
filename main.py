import streamlit as st
from utils import init_page
from components.modal import show_modal

init_page()

st.title("我是test")

# 固定按鈕
if st.button("點擊我"):
    show_modal("這是一個對話框", "這是對話框的內容。")