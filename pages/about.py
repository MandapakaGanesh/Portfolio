"""
About Me page — Enhanced professional design with rich color palette.
"""

import streamlit as st
from components.data import (
    PERSONAL, EDUCATION, INTERESTS, TOOLS,
    CERTIFICATES, ACHIEVEMENTS, CERTIFICATE_LINKS
)
from components.styles import section_header
from datetime import datetime


def _parse_date(date_str):
    """Parse 'Mon YYYY' to sortable datetime. Returns min date on failure."""
    try:
        return datetime.strptime(date_str.strip(), "%b %Y")
    except Exception:
        return datetime.min


def render_about():

    # ── Page CSS ──────────────────────────────────────────────────────────────
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

    :root {
        --gold:        #C9973A;
        --gold-light:  #E8BE6A;
        --gold-dim:    rgba(201,151,58,0.14);
        --teal:        #00C2D4;
        --teal-dim:    rgba(0,194,212,0.1);
        --emerald:     #00C896;
        --rose:        #FF6B8A;
        --navy-card:   #0F1829;
        --navy-hover:  #131E30;
        --mist:        #A8C0D6;
        --steel:       #607A94;
        --ivory:       #F2EDE4;
        --border:      rgba(201,151,58,0.15);
    }

    /* ── Bio card ── */
    .bio-card {
        background: linear-gradient(145deg, #0F1829, #131E30);
        border: 1px solid var(--border);
        border-left: 4px solid var(--gold);
        border-radius: 0 16px 16px 0;
        padding: 2rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .bio-card::after {
        content: '';
        position: absolute;
        top: -30%;
        right: -10%;
        width: 250px;
        height: 250px;
        background: radial-gradient(circle, rgba(201,151,58,0.06), transparent 70%);
        pointer-events: none;
    }

    /* ── Section header ── */
    .about-section-label {
        font-size: 0.65rem;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        color: var(--gold);
        font-weight: 600;
        margin-bottom: 0.3rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .about-section-label::after {
        content: '';
        flex: 1;
        max-width: 50px;
        height: 1px;
        background: linear-gradient(90deg, var(--gold), transparent);
    }
    .about-section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: var(--ivory);
        margin-bottom: 1.5rem;
        letter-spacing: -0.01em;
    }
    .grad-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(201,151,58,0.25), rgba(0,194,212,0.15), transparent);
        margin: 2.5rem 0;
        border: none;
    }

    /* ── Timeline ── */
    .timeline-wrap {
        position: relative;
        padding-left: 2rem;
    }
    .timeline-wrap::before {
        content: '';
        position: absolute;
        left: 6px;
        top: 8px;
        bottom: 0;
        width: 2px;
        background: linear-gradient(180deg, var(--gold), rgba(201,151,58,0.1));
    }
    .tl-item {
        position: relative;
        margin-bottom: 2rem;
        padding: 1.2rem 1.4rem;
        background: linear-gradient(145deg, #0F1829, #131E30);
        border: 1px solid var(--border);
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    .tl-item::before {
        content: '';
        position: absolute;
        left: -1.85rem;
        top: 1.4rem;
        width: 12px;
        height: 12px;
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        border-radius: 50%;
        border: 2px solid #080C18;
        box-shadow: 0 0 10px rgba(201,151,58,0.5);
    }
    .tl-item:hover {
        border-color: rgba(201,151,58,0.35);
        transform: translateX(4px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    .tl-year {
        font-family: 'DM Mono', monospace;
        font-size: 0.7rem;
        color: var(--gold);
        letter-spacing: 0.1em;
        margin-bottom: 0.4rem;
    }
    .tl-degree {
        font-size: 1rem;
        font-weight: 600;
        color: var(--ivory);
        margin-bottom: 0.25rem;
    }
    .tl-school {
        font-size: 0.85rem;
        color: var(--gold-light);
        margin-bottom: 0.2rem;
    }
    .tl-detail {
        font-family: 'DM Mono', monospace;
        font-size: 0.75rem;
        color: var(--steel);
    }

    /* ── Interest cards ── */
    .interest-card {
        background: linear-gradient(145deg, #0F1829, #131E30);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 1.4rem 1rem;
        text-align: center;
        transition: all 0.35s ease;
        position: relative;
        overflow: hidden;
        height: 100%;
    }
    .interest-card::before {
        content: '';
        position: absolute;
        bottom: 0; left: 0;
        width: 100%; height: 3px;
        background: linear-gradient(90deg, var(--gold), var(--teal));
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.35s ease;
    }
    .interest-card:hover {
        border-color: rgba(201,151,58,0.3);
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.35);
    }
    .interest-card:hover::before { transform: scaleX(1); }

    /* ── Tool badges ── */
    .tool-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(0,194,212,0.07);
        border: 1px solid rgba(0,194,212,0.18);
        border-radius: 10px;
        padding: 7px 14px;
        margin: 4px;
        font-size: 0.83rem;
        color: #A8C0D6;
        transition: all 0.25s ease;
    }
    .tool-badge:hover {
        background: rgba(0,194,212,0.13);
        border-color: rgba(0,194,212,0.35);
        color: #00C2D4;
        transform: translateY(-2px);
    }

    /* ── Certificate cards ── */
    .cert-card {
        background: linear-gradient(145deg, #0F1829, #131E30);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 1.4rem;
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        margin-bottom: 1rem;
        transition: all 0.35s ease;
        position: relative;
        overflow: hidden;
    }
    .cert-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 3px; height: 100%;
        background: linear-gradient(180deg, var(--teal), var(--gold));
        opacity: 0;
        transition: opacity 0.35s ease;
    }
    .cert-card:hover {
        border-color: rgba(0,194,212,0.3);
        transform: translateX(4px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    }
    .cert-card:hover::before { opacity: 1; }
    .cert-badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: rgba(201,151,58,0.07);
        border: 1px solid rgba(201,151,58,0.2);
        color: var(--gold);
        font-size: 0.68rem;
        padding: 3px 10px;
        border-radius: 20px;
        font-weight: 500;
        letter-spacing: 0.05em;
        margin-top: 0.5rem;
    }
    .view-cert-btn {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        margin-top: 0.7rem;
        font-size: 0.73rem;
        letter-spacing: 0.05em;
        color: var(--teal);
        text-decoration: none;
        border: 1px solid rgba(0,194,212,0.25);
        padding: 0.35rem 0.8rem;
        border-radius: 6px;
        background: rgba(0,194,212,0.05);
        transition: all 0.3s ease;
    }
    .view-cert-btn:hover {
        background: rgba(0,194,212,0.12);
        border-color: rgba(0,194,212,0.5);
        color: #00C2D4;
    }

    /* ── Achievement timeline ── */
    .ach-item {
        background: linear-gradient(145deg, #0F1829, #131E30);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
        display: flex;
        gap: 1rem;
        align-items: flex-start;
        transition: all 0.3s ease;
    }
    .ach-item:hover {
        border-color: rgba(201,151,58,0.3);
        transform: translateX(4px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
    }
    .ach-icon-wrap {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        background: var(--gold-dim);
        border: 1px solid rgba(201,151,58,0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        flex-shrink: 0;
    }

    /* ── Beyond card ── */
    .beyond-card {
        background: linear-gradient(135deg, rgba(201,151,58,0.06), rgba(0,194,212,0.04));
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── Header ────────────────────────────────────────────────────────────────
    st.markdown(section_header("Personal", "About Me"), unsafe_allow_html=True)

    # ── Bio card ──────────────────────────────────────────────────────────────
    st.markdown(
        "<div class='bio-card'>"
        "<p style='font-family:Cormorant Garamond,serif;font-size:1.22rem;"
        "font-weight:300;font-style:italic;color:#F2EDE4;line-height:1.85;margin:0 0 1rem;'>"
        "\"" + PERSONAL['intro'] + "\"</p>"
        "<div style='display:flex;gap:1.5rem;flex-wrap:wrap;align-items:center;'>"
        "<span style='display:flex;align-items:center;gap:5px;font-size:0.8rem;color:#607A94;'>"
        "📍 " + PERSONAL['location'] + "</span>"
        "<span style='display:flex;align-items:center;gap:5px;font-size:0.8rem;color:#607A94;'>"
        "✉️ " + PERSONAL['email'] + "</span>"
        "<span style='display:inline-flex;align-items:center;gap:5px;"
        "background:rgba(0,200,150,0.1);border:1px solid rgba(0,200,150,0.25);"
        "color:#00C896;font-size:0.75rem;padding:3px 10px;border-radius:20px;font-weight:500;'>"
        "<span style='width:6px;height:6px;background:#00C896;border-radius:50%;"
        "box-shadow:0 0 6px #00C896;display:inline-block;'></span>"
        + PERSONAL['status'] + "</span>"
        "</div></div>",
        unsafe_allow_html=True,
    )

    # ── Education ─────────────────────────────────────────────────────────────
    st.markdown(
        "<div class='about-section-label'>Academic Background</div>"
        "<div class='about-section-title'>Education</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='timeline-wrap'>", unsafe_allow_html=True)
    for edu in EDUCATION:
        st.markdown(
            "<div class='tl-item'>"
            "<div class='tl-year'>" + edu['year'] + "</div>"
            "<div class='tl-degree'>" + edu['icon'] + " " + edu['degree'] + "</div>"
            "<div class='tl-school'>" + edu['school'] + "</div>"
            "<div class='tl-detail'>" + edu['detail'] + "</div>"
            "</div>",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # ── Career interests ──────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='about-section-label'>What Drives Me</div>"
        "<div class='about-section-title'>Career Interests</div>",
        unsafe_allow_html=True,
    )

    int_cols = st.columns(len(INTERESTS))
    interest_colors = ["#C9973A", "#00C2D4", "#00C896", "#FF6B8A", "#C9973A"]
    for col, (icon, title, desc), color in zip(int_cols, INTERESTS, interest_colors):
        with col:
            st.markdown(
                "<div class='interest-card'>"
                "<div style='font-size:2rem;margin-bottom:0.6rem;'>" + icon + "</div>"
                "<div style='font-size:0.88rem;font-weight:600;color:#F2EDE4;"
                "margin-bottom:0.4rem;'>" + title + "</div>"
                "<div style='font-size:0.76rem;color:#607A94;line-height:1.6;'>"
                + desc + "</div>"
                "</div>",
                unsafe_allow_html=True,
            )

    # ── Tools & Technologies ──────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='about-section-label'>Technical Arsenal</div>"
        "<div class='about-section-title'>Tools &amp; Technologies</div>",
        unsafe_allow_html=True,
    )

    badges = "".join(
        "<span class='tool-badge'>" + icon + " " + name + "</span>"
        for icon, name in TOOLS
    )
    st.markdown(
        "<div style='line-height:3.2;'>" + badges + "</div>",
        unsafe_allow_html=True,
    )

    # ── Certificates (sorted recent first) ───────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='about-section-label'>Credentials</div>"
        "<div class='about-section-title'>Certificates</div>",
        unsafe_allow_html=True,
    )

    # Sort by date descending — most recent first
    sorted_certs = sorted(
        CERTIFICATES,
        key=lambda c: _parse_date(c['date']),
        reverse=True,
    )

    cert_cols = st.columns(2, gap="large")
    for i, cert in enumerate(sorted_certs):
        with cert_cols[i % 2]:
            cert_link = CERTIFICATE_LINKS.get(cert['title'])
            link_html = (
                '<a href="' + cert_link + '" target="_blank" class="view-cert-btn">'
                '📄 View Certificate</a>'
            ) if cert_link else ""

            st.markdown(
                "<div class='cert-card'>"
                "<div style='font-size:2.2rem;flex-shrink:0;'>" + cert['icon'] + "</div>"
                "<div style='flex:1;'>"
                "<div style='font-size:0.95rem;font-weight:600;color:#F2EDE4;"
                "margin-bottom:0.25rem;line-height:1.4;'>" + cert['title'] + "</div>"
                "<div style='font-size:0.82rem;color:var(--gold-light);margin-bottom:0.2rem;'>"
                + cert['issuer'] + "</div>"
                "<div class='cert-badge'>🗓 " + cert['date'] + "</div>"
                + link_html +
                "</div></div>",
                unsafe_allow_html=True,
            )

    # ── Achievements ──────────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='about-section-label'>Milestones</div>"
        "<div class='about-section-title'>Achievements</div>",
        unsafe_allow_html=True,
    )

    for ach in ACHIEVEMENTS:
        st.markdown(
            "<div class='ach-item'>"
            "<div class='ach-icon-wrap'>" + ach['icon'] + "</div>"
            "<div>"
            "<div style='font-family:DM Mono,monospace;font-size:0.7rem;"
            "color:var(--gold);margin-bottom:0.3rem;letter-spacing:0.08em;'>"
            + ach['date'] + "</div>"
            "<div style='font-size:0.98rem;font-weight:600;color:#F2EDE4;"
            "margin-bottom:0.3rem;'>" + ach['title'] + "</div>"
            "<div style='font-size:0.84rem;color:#607A94;line-height:1.65;'>"
            + ach['detail'] + "</div>"
            "</div></div>",
            unsafe_allow_html=True,
        )

    # ── Beyond the Data ───────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='beyond-card'>"
        "<div class='about-section-label' style='margin-bottom:0.6rem;'>Beyond the Data</div>"
        "<p style='color:#A8C0D6;line-height:1.85;font-size:0.95rem;margin:0;'>"
        "When I'm not wrangling datasets or building dashboards, I enjoy exploring "
        "competitive programming challenges, staying current with developments in "
        "AI and data science, and contributing to collaborative projects. "
        "I believe curiosity and adaptability are just as important as technical "
        "skills — and I bring both to every problem I tackle."
        "</p></div>",
        unsafe_allow_html=True,
    )