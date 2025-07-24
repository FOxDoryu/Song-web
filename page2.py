import streamlit as st

st.set_page_config(page_title="หน้าสอง", layout="centered")

st.title("Page2")
st.write("SONG : Timeless")

if st.button("Retrun", use_container_width=True):
    st.session_state.page = "home"

if st.session_state.get("page") == "home":
    st.experimental_rerun()
