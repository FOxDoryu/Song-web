import streamlit as st

st.set_page_config(page_title="หน้าแรก", layout="centered")

st.markdown("<h1 style='text-align: center;'>Welcome</h1>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("Run", key="run_button", use_container_width=True):
    st.session_state.page = "page2"

if st.session_state.get("page") == "page2":
    st.experimental_rerun()
