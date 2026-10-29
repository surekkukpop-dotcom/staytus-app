import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Status AI - Stray Kids Edition",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    iframe { width: 100% !important; height: 95vh !important; border: none !important; }
</style>
""", unsafe_allow_html=True)

# Load HTML from separate file
with open('app_index.html', 'r', encoding='utf-8') as f:
    html_code = f.read()

components.html(html_code, height=880, scrolling=True)
