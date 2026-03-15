"""
Resume page — Enhanced professional design with download UI.
"""

import base64
import os
import streamlit as st
import streamlit.components.v1 as components
from components.data import PERSONAL
from components.styles import section_header


def _load_asset(filename: str) -> bytes | None:
    path = os.path.join(os.path.dirname(__file__), "..", "assets", filename)
    try:
        with open(path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        return None


def render_resume():

    st.markdown("""
    <style>
    .resume-info-bar {
        display: flex; align-items: center;
        justify-content: space-between;
        background: linear-gradient(145deg, #0F1829, #131E30);
        border: 1px solid rgba(201,151,58,0.2);
        border-radius: 14px;
        padding: 1.2rem 1.6rem;
        margin-bottom: 1.5rem;
    }
    .resume-icon-box {
        width: 46px; height: 46px;
        background: linear-gradient(135deg, #C9973A, #E8BE6A);
        border-radius: 12px;
        display: flex; align-items: center;
        justify-content: center; font-size: 1.4rem;
        box-shadow: 0 4px 16px rgba(201,151,58,0.35);
        flex-shrink: 0;
    }
    .resume-status-dot {
        width: 8px; height: 8px;
        background: #00C896; border-radius: 50%;
        box-shadow: 0 0 8px #00C896;
        display: inline-block; margin-right: 6px;
    }
    .download-strip {
        background: linear-gradient(135deg,
            rgba(201,151,58,0.06), rgba(0,194,212,0.04));
        border: 1px solid rgba(201,151,58,0.15);
        border-radius: 14px;
        padding: 1.4rem 1.8rem;
        display: flex; align-items: center;
        gap: 1.5rem; flex-wrap: wrap;
        margin-bottom: 1.2rem;
    }
    .contact-chip {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(15,24,41,0.8);
        border: 1px solid rgba(201,151,58,0.15);
        border-radius: 10px; padding: 0.55rem 1rem;
        color: #A8C0D6; text-decoration: none;
        font-size: 0.8rem; transition: all 0.25s ease;
    }
    .contact-chip:hover {
        border-color: rgba(201,151,58,0.35);
        color: #C9973A;
    }
    .grad-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent,
            rgba(201,151,58,0.25), rgba(0,194,212,0.15), transparent);
        margin: 1.5rem 0; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(section_header("Curriculum Vitae", "Resume"), unsafe_allow_html=True)

    pdf_bytes = _load_asset(PERSONAL["resume_file"])
    img_bytes = _load_asset(PERSONAL.get("resume_image", ""))

    # ── Info bar ──────────────────────────────────────────────────────────────
    st.markdown(
        "<div class='resume-info-bar'>"
        "<div style='display:flex;align-items:center;gap:1rem;'>"
        "<div class='resume-icon-box'>📄</div>"
        "<div>"
        "<div style='font-size:1rem;font-weight:600;color:#F2EDE4;'>"
        "Mandapaka Ganesh — Resume</div>"
        "<div style='font-size:0.75rem;color:#607A94;margin-top:2px;'>"
        "Data Science &amp; Analytics · Updated 2025</div>"
        "</div></div>"
        "<div style='display:flex;align-items:center;gap:6px;'>"
        "<span class='resume-status-dot'></span>"
        "<span style='font-size:0.78rem;color:#00C896;font-weight:500;'>"
        "Available for Opportunities</span>"
        "</div></div>",
        unsafe_allow_html=True,
    )

    # ── Download button (top) ─────────────────────────────────────────────────
    if pdf_bytes:
        col_l, col_btn, col_r = st.columns([1, 2, 1])
        with col_btn:
            st.download_button(
                label="📥  Download Resume PDF",
                data=pdf_bytes,
                file_name="Mandapaka_Ganesh_Resume.pdf",
                mime="application/pdf",
                key="resume_download_top",
                use_container_width=True,
            )
    else:
        st.warning(f"⚠️ Resume PDF not found — place it at `assets/{PERSONAL['resume_file']}`")

    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)

    # ── Resume viewer ─────────────────────────────────────────────────────────
    if img_bytes:
        b64_img = base64.b64encode(img_bytes).decode("utf-8")
        resume_html = """
        <!DOCTYPE html><html><head>
        <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body { background: transparent; font-family: 'DM Sans', sans-serif;
               overflow-y: auto; overflow-x: hidden; }
        .toolbar {
            display: flex; align-items: center; justify-content: space-between;
            background: linear-gradient(135deg, rgba(15,24,41,0.98), rgba(8,12,24,0.98));
            border: 1px solid rgba(201,151,58,0.25);
            border-radius: 12px 12px 0 0;
            padding: 0.7rem 1.2rem;
            position: sticky; top: 0; z-index: 100;
        }
        .toolbar-title { font-size: 0.85rem; font-weight: 600; color: #F2EDE4; }
        .toolbar-sub   { font-size: 0.7rem; color: #607A94; margin-top: 1px; }
        .badge {
            font-size: 0.7rem; padding: 0.28rem 0.7rem;
            border-radius: 20px; font-weight: 500;
        }
        .badge-gold  { background: rgba(201,151,58,0.15);
                       border: 1px solid rgba(201,151,58,0.35); color: #C9973A; }
        .badge-green { background: rgba(0,200,150,0.12);
                       border: 1px solid rgba(0,200,150,0.3); color: #00C896; }
        .viewer {
            background: #080C18;
            border: 1px solid rgba(201,151,58,0.15); border-top: none;
            border-radius: 0 0 14px 14px;
            padding: 2rem 2rem 2.5rem;
            display: flex; flex-direction: column; align-items: center; gap: 1rem;
        }
        .page-wrap {
            width: 100%; max-width: 860px;
            background: #fff; border-radius: 6px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.07),
                        0 10px 40px rgba(0,0,0,0.4),
                        0 0 0 1px rgba(201,151,58,0.1);
            overflow: hidden; transition: box-shadow 0.3s ease;
        }
        .page-wrap:hover {
            box-shadow: 0 8px 12px rgba(0,0,0,0.1),
                        0 20px 60px rgba(0,0,0,0.5),
                        0 0 0 1px rgba(201,151,58,0.25),
                        0 0 30px rgba(201,151,58,0.08);
        }
        .resume-img { width: 100%; height: auto; display: block; }
        .page-label { font-size: 0.7rem; color: #607A94;
                      letter-spacing: 0.1em; text-transform: uppercase; }
        .footer-row {
            display: flex; align-items: center; justify-content: center;
            gap: 1.5rem; padding: 0.5rem 0;
        }
        .footer-item { font-size: 0.73rem; color: #607A94; }
        .sep { width: 4px; height: 4px; background: rgba(201,151,58,0.4);
               border-radius: 50%; }
        </style></head><body>
        <div class="toolbar">
            <div>
                <div class="toolbar-title">Mandapaka_Ganesh_Resume.pdf</div>
                <div class="toolbar-sub">Page 1 of 1</div>
            </div>
            <div style="display:flex;gap:6px;">
                <span class="badge badge-green">● Open to Work</span>
                <span class="badge badge-gold">2025</span>
            </div>
        </div>
        <div class="viewer">
            <div class="page-wrap">
                <img class="resume-img"
                     src="data:image/jpeg;base64,""" + b64_img + """"
                     alt="Resume — Mandapaka Ganesh" />
            </div>
            <div class="page-label">Page 1</div>
            <div class="footer-row">
                <span class="footer-item">📍 Phagwara, Punjab, IN</span>
                <div class="sep"></div>
                <span class="footer-item">✉️ ganeshmandapaka06@gmail.com</span>
                <div class="sep"></div>
                <span class="footer-item">🐙 github.com/MandapakaGanesh</span>
            </div>
        </div>
        </body></html>
        """
        components.html(resume_html, height=1460, scrolling=False)

    else:
        st.markdown(
            "<div style='background:linear-gradient(145deg,#0F1829,#131E30);"
            "border:2px dashed rgba(201,151,58,0.25);border-radius:14px;"
            "padding:4rem 2rem;text-align:center;'>"
            "<div style='font-size:3rem;margin-bottom:1rem;'>📄</div>"
            "<div style='font-size:1.1rem;font-weight:600;color:#F2EDE4;"
            "margin-bottom:0.5rem;'>Resume Preview Unavailable</div>"
            "<div style='font-size:0.88rem;color:#607A94;line-height:1.7;'>"
            "Add the resume image to the assets/ folder to enable preview."
            "</div></div>",
            unsafe_allow_html=True,
        )

    # ── Download strip ────────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='download-strip'>"
        "<div style='flex:1;min-width:200px;'>"
        "<div style='font-size:0.95rem;font-weight:600;color:#F2EDE4;"
        "margin-bottom:0.3rem;'>📥 Save a Copy</div>"
        "<div style='font-size:0.82rem;color:#607A94;line-height:1.6;'>"
        "Download the full PDF for offline access or to share with recruiters."
        "</div></div></div>",
        unsafe_allow_html=True,
    )

    if pdf_bytes:
        col_l2, col_btn2, col_r2 = st.columns([1, 2, 1])
        with col_btn2:
            st.download_button(
                label="📥  Download Resume PDF",
                data=pdf_bytes,
                file_name="Mandapaka_Ganesh_Resume.pdf",
                mime="application/pdf",
                key="resume_download_bottom",
                use_container_width=True,
            )

    # ── Contact chips ─────────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div style='display:flex;gap:0.8rem;flex-wrap:wrap;justify-content:center;'>"
        '<a href="mailto:' + PERSONAL['email'] + '" class="contact-chip">'
        "✉️ " + PERSONAL['email'] + "</a>"
        '<a href="' + PERSONAL['linkedin'] + '" target="_blank" class="contact-chip">'
        "💼 LinkedIn Profile</a>"
        '<a href="' + PERSONAL['github'] + '" target="_blank" class="contact-chip">'
        "⭐ GitHub</a>"
        "</div>",
        unsafe_allow_html=True,
    )