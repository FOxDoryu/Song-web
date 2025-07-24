import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title="หน้าแรก", layout="centered")

st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
    .run-button button {
        font-size: 24px !important;
        padding: 1em 2em;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="center"><div class="run-button">', unsafe_allow_html=True)
if st.button("Run"):
    switch_page("page2")
st.markdown('</div></div>', unsafe_allow_html=True)
