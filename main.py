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
        font-size: 30px !important;
        padding: 1.5em 3em;
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
if st.button("Run"):
    st.switch_page("Page2")
st.markdown('</div></div>', unsafe_allow_html=True)
