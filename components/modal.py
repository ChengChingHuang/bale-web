import streamlit as st

def show_modal(title, content):
    with st.expander(title):
        st.markdown(content)

def open_modal():
    st.session_state['modal_open'] = True
