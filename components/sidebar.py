"""
Sidebar navigation component — professional sleek design.
"""

import streamlit as st
from components.data import PERSONAL


PAGES = ["Home", "About", "Projects", "Skills", "Resume", "Contact"]

PAGE_ICONS = {
    "Home":     "🏠",
    "About":    "👤",
    "Projects": "🗂️",
    "Skills":   "📊",
    "Resume":   "📄",
    "Contact":  "✉️",
}


def render_sidebar():
    """Renders a professional sidebar. Returns selected page."""

    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

    st.markdown("""
    <style>
    section[data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: none !important;
        border-radius: 10px !important;
        color: #8BA3C7 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.06em !important;
        text-transform: uppercase !important;
        padding: 0.6rem 1rem !important;
        text-align: left !important;
        transition: all 0.25s ease !important;
        width: 100% !important;
        margin-bottom: 2px !important;
        box-shadow: none !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(212,175,55,0.08) !important;
        color: #D4AF37 !important;
        transform: translateX(4px) !important;
        box-shadow: none !important;
        border-left: 2px solid rgba(212,175,55,0.5) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:

        st.markdown(
            "<div style='text-align:center;padding:2rem 1rem 1.5rem;"
            "border-bottom:1px solid rgba(212,175,55,0.2);'>"
            "<div style='width:88px;height:88px;border-radius:50%;"
            "background:linear-gradient(135deg,#162032,#1F2F45);"
            "border:2px solid rgba(212,175,55,0.5);"
            "display:flex;align-items:center;justify-content:center;"
            "font-size:2.4rem;margin:0 auto 1rem;"
            "box-shadow:0 0 25px rgba(212,175,55,0.15),0 8px 24px rgba(0,0,0,0.4);'>"
            "👨‍💻</div>"
            "<p style='font-family:Cormorant Garamond,serif;font-size:1.15rem;"
            "font-weight:400;color:#F8F5F0;margin:0 0 0.2rem;line-height:1.3;'>"
            + PERSONAL['name_first'] + "<br>" + PERSONAL['name_last'] + "</p>"
            "<p style='font-size:0.65rem;letter-spacing:0.15em;text-transform:uppercase;"
            "color:#D4AF37;font-weight:500;margin:0 0 0.8rem;'>"
            + PERSONAL['title'] + "</p>"
            "<div style='display:inline-flex;align-items:center;gap:6px;"
            "background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);"
            "color:#10B981;font-size:0.67rem;padding:4px 12px;"
            "border-radius:20px;font-weight:500;letter-spacing:0.05em;'>"
            "<span style='width:6px;height:6px;background:#10B981;"
            "border-radius:50%;display:inline-block;box-shadow:0 0 6px #10B981;'></span>"
            + PERSONAL['status'] + "</div>"
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='font-size:0.63rem;letter-spacing:0.22em;text-transform:uppercase;"
            "color:rgba(212,175,55,0.55);padding:1.2rem 0.5rem 0.4rem;"
            "margin:0;font-weight:600;'>Navigation</p>",
            unsafe_allow_html=True,
        )

        for page in PAGES:
            icon = PAGE_ICONS[page]
            is_active = st.session_state.current_page == page

            if is_active:
                st.markdown(
                    "<div style='display:flex;align-items:center;gap:0.7rem;"
                    "background:linear-gradient(90deg,rgba(212,175,55,0.14),transparent);"
                    "border-left:3px solid #D4AF37;border-radius:0 10px 10px 0;"
                    "padding:0.6rem 1rem;margin-bottom:2px;'>"
                    "<span style='font-size:0.95rem;'>" + icon + "</span>"
                    "<span style='font-size:0.85rem;font-weight:600;"
                    "color:#D4AF37;letter-spacing:0.06em;text-transform:uppercase;'>"
                    + page + "</span>"
                    "<span style='margin-left:auto;width:6px;height:6px;"
                    "background:#D4AF37;border-radius:50%;"
                    "box-shadow:0 0 8px #D4AF37;'></span>"
                    "</div>",
                    unsafe_allow_html=True,
                )
            else:
                if st.button(
                    f"{icon}  {page}",
                    key=f"nav_{page}",
                    use_container_width=True,
                ):
                    st.session_state.current_page = page
                    st.rerun()

        st.markdown(
            "<div style='height:1px;background:linear-gradient(90deg,"
            "transparent,rgba(212,175,55,0.3),transparent);margin:1.2rem 0;'></div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='font-size:0.63rem;letter-spacing:0.22em;text-transform:uppercase;"
            "color:rgba(212,175,55,0.55);padding:0 0.5rem 0.6rem;"
            "margin:0;font-weight:600;'>Connect</p>",
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                '<a href="' + PERSONAL["github"] + '" target="_blank" '
                'style="display:flex;align-items:center;justify-content:center;'
                'gap:5px;background:rgba(212,175,55,0.07);'
                'border:1px solid rgba(212,175,55,0.25);border-radius:8px;'
                'padding:8px 4px;font-size:0.73rem;color:#D4AF37;'
                'text-decoration:none;">⭐ GitHub</a>',
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                '<a href="' + PERSONAL["linkedin"] + '" target="_blank" '
                'style="display:flex;align-items:center;justify-content:center;'
                'gap:5px;background:rgba(212,175,55,0.07);'
                'border:1px solid rgba(212,175,55,0.25);border-radius:8px;'
                'padding:8px 4px;font-size:0.73rem;color:#D4AF37;'
                'text-decoration:none;">💼 LinkedIn</a>',
                unsafe_allow_html=True,
            )

        st.markdown(
            "<div style='text-align:center;padding:1.5rem 0 0.5rem;'>"
            "<p style='font-size:0.62rem;color:rgba(139,163,199,0.35);"
            "letter-spacing:0.08em;margin:0;'>© 2026 " + PERSONAL['name'] + "</p>"
            "</div>",
            unsafe_allow_html=True,
        )

    return st.session_state.current_page