import streamlit as st
from streamlit_extras.switch_page_button import switch_page

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    import home
elif st.session_state.page == "page2":
    import page2