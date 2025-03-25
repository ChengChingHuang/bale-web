import streamlit as st

def menu():
    st.sidebar.title("主選單")
    st.sidebar.page_link(page="main.py", label="首頁", icon="🏠")
    st.sidebar.markdown("---")
    st.sidebar.title("附選單")
    st.sidebar.page_link(page="pages/bagging.py", label="套袋資訊", icon="📦")
    st.sidebar.page_link(page="pages/about_guava.py", label="芭樂資訊", icon="🍈")
    st.sidebar.page_link(page="pages/contact_info.py", label="聯絡資訊", icon="📞")
    st.sidebar.page_link(page="pages/assistant.py", label="助手", icon="🤖")
    st.sidebar.markdown("---")