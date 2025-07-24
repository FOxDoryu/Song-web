import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    import home
elif st.session_state.page == "page2":
    import page2
