import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="หน้า 2", layout="wide")

st.title("Page 2")

st.write("SONG : Timeless")

st.markdown(
    """
    <style>
    .back-button {
        position: fixed;
        bottom: 20px;
        left: 20px;
    }
    .back-button button {
        background-color: #f44336;
        color: white;
        font-size: 18px;
        padding: 0.5em 1.5em;
        border: none;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="back-button">', unsafe_allow_html=True)
if st.button("← Back"):
    switch_page("main")
st.markdown('</div>', unsafe_allow_html=True)
