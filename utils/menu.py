import streamlit as st


def menu():
    st.sidebar.title("主選單")
    st.sidebar.markdown("---")
    st.sidebar.title("附選單")
    st.sidebar.page_link(page="pages/test.py", label="測試", icon="📚")
    st.sidebar.markdown("---")