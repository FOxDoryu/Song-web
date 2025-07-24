import streamlit as st

st.set_page_config(page_title="หน้า 2", layout="wide")

st.title("Page2")
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
        padding: 0.6em 1.2em;
        border: none;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="back-button">', unsafe_allow_html=True)
st.page_link("main", label="Back", icon="⬅️")
st.markdown('</div>', unsafe_allow_html=True)
