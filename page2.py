import streamlit as st

st.set_page_config(page_title="Page2", layout="wide")

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
        background-color: #DC143C;
        color: white;
        font-size: 20px;
        padding: 0.7em 2em;
        border: none;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="back-button">', unsafe_allow_html=True)
if st.button("Back"):
    st.switch_page("main")
st.markdown('</div>', unsafe_allow_html=True)
