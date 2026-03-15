"""
Main entry point for the Data Science Portfolio application.
Run with: streamlit run main2.py
"""

import streamlit as st

st.set_page_config(
    page_title="Mandapaka Ganesh · Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={},
)

from components.styles import load_css
from components.sidebar import render_sidebar
from pages.home     import render_home
from pages.about    import render_about
from pages.projects import render_projects
from pages.skills   import render_skills
from pages.resume   import render_resume
from pages.contact  import render_contact

st.markdown(load_css(), unsafe_allow_html=True)

# ── Professional background ───────────────────────────────────────────────────
st.markdown("""
<style>
/* Target every possible Streamlit container */
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > section,
.main {
    background-color: #060A14 !important;
    background-image:
        radial-gradient(ellipse 60% 45% at 0% 0%,
            rgba(201,151,58,0.18) 0%, transparent 50%),
        radial-gradient(ellipse 50% 40% at 100% 0%,
            rgba(0,194,212,0.14) 0%, transparent 48%),
        radial-gradient(ellipse 60% 45% at 100% 100%,
            rgba(201,151,58,0.12) 0%, transparent 50%),
        radial-gradient(ellipse 50% 40% at 0% 100%,
            rgba(0,200,150,0.10) 0%, transparent 48%) !important;
    background-attachment: fixed !important;
}

/* Dot grid */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: radial-gradient(
        circle, rgba(201,151,58,0.12) 1px, transparent 1px
    );
    background-size: 35px 35px;
    pointer-events: none;
    z-index: 0;
}

/* Keep all content above the dot grid */
[data-testid="stAppViewContainer"] > section.main {
    position: relative;
    z-index: 1;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0C1525 0%, #080E1C 100%) !important;
}
</style>
""", unsafe_allow_html=True)

# ── Initialise page ───────────────────────────────────────────────────────────
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# ── Render sidebar ────────────────────────────────────────────────────────────
render_sidebar()

# ── Router ────────────────────────────────────────────────────────────────────
PAGE_MAP = {
    "Home":     render_home,
    "About":    render_about,
    "Projects": render_projects,
    "Skills":   render_skills,
    "Resume":   render_resume,
    "Contact":  render_contact,
}

PAGE_MAP.get(st.session_state.current_page, render_home)()