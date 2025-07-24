import streamlit as st

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
        font-size: 28px !important;
        padding: 1.2em 2em;
        background-color: #1E90FF;
        color: white;
        border: none;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="center"><div class="run-button">', unsafe_allow_html=True)
st.page_link("pages/Page2.py", label="Run", icon="▶️")
st.markdown('</div></div>', unsafe_allow_html=True)
