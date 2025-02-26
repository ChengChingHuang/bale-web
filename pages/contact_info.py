import streamlit as st
from utils import init_page
init_page()

st.title("聯絡資訊")
st.write("這是關於聯絡資訊的內容。")

# 固定按鈕
if st.button("點擊我"):
    st.modal("這是一個對話框", "這是對話框的內容。")
