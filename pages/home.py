"""
Home page — Enhanced professional design with rich color palette.
"""

import streamlit as st
from components.data import PERSONAL, STATS


def render_home():

    # ── Page-level CSS ────────────────────────────────────────────────────────
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

    /* ── Palette ── */
    :root {
        --navy:        #080C18;
        --navy-mid:    #0F1829;
        --navy-card:   #131E30;
        --navy-hover:  #1A2740;
        --gold:        #C9973A;
        --gold-light:  #E8BE6A;
        --gold-dim:    rgba(201,151,58,0.18);
        --teal:        #00C2D4;
        --teal-dim:    rgba(0,194,212,0.12);
        --emerald:     #00C896;
        --emerald-dim: rgba(0,200,150,0.12);
        --rose:        #FF6B8A;
        --rose-dim:    rgba(255,107,138,0.12);
        --mist:        #A8C0D6;
        --steel:       #607A94;
        --ivory:       #F2EDE4;
        --border:      rgba(201,151,58,0.15);
    }

    /* ── Animated gradient background ── */
    .home-hero-bg {
        position: relative;
    }
    .home-hero-bg::before {
        content: '';
        position: fixed;
        top: -50%;
        left: -10%;
        width: 60%;
        height: 80%;
        background: radial-gradient(ellipse, rgba(201,151,58,0.04) 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }

    /* ── Hero avatar ── */
    .avatar-ring {
        width: 210px;
        height: 210px;
        border-radius: 50%;
        background: linear-gradient(145deg, #0F1829, #1A2740);
        border: 2px solid transparent;
        background-clip: padding-box;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 5.5rem;
        box-shadow:
            0 0 0 1px rgba(201,151,58,0.3),
            0 0 40px rgba(201,151,58,0.12),
            0 20px 60px rgba(0,0,0,0.6);
        animation: floatAvatar 4s ease-in-out infinite;
    }
    .avatar-ring::before {
        content: '';
        position: absolute;
        inset: -2px;
        border-radius: 50%;
        background: conic-gradient(
            from 0deg,
            rgba(201,151,58,0.8),
            rgba(0,194,212,0.6),
            rgba(201,151,58,0.2),
            rgba(201,151,58,0.8)
        );
        z-index: -1;
        animation: rotateBorder 6s linear infinite;
    }
    .avatar-status {
        position: absolute;
        bottom: 12px;
        right: 12px;
        width: 22px;
        height: 22px;
        background: #00C896;
        border-radius: 50%;
        border: 3px solid #080C18;
        box-shadow: 0 0 12px #00C896, 0 0 24px rgba(0,200,150,0.4);
        animation: pulseDot 2s ease-in-out infinite;
    }
    @keyframes floatAvatar {
        0%, 100% { transform: translateY(0px); }
        50%       { transform: translateY(-12px); }
    }
    @keyframes rotateBorder {
        from { transform: rotate(0deg); }
        to   { transform: rotate(360deg); }
    }
    @keyframes pulseDot {
        0%, 100% { box-shadow: 0 0 12px #00C896, 0 0 24px rgba(0,200,150,0.4); }
        50%       { box-shadow: 0 0 20px #00C896, 0 0 40px rgba(0,200,150,0.6); }
    }

    /* ── Hero text ── */
    .hero-eyebrow {
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.28em;
        text-transform: uppercase;
        color: var(--gold);
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .hero-eyebrow::before {
        content: '';
        display: inline-block;
        width: 30px;
        height: 1px;
        background: var(--gold);
        opacity: 0.6;
    }
    .hero-name-enhanced {
        font-family: 'Cormorant Garamond', serif;
        font-size: 4.8rem;
        font-weight: 300;
        line-height: 1.05;
        margin-bottom: 0.6rem;
        background: linear-gradient(135deg, #F2EDE4 0%, #C9973A 45%, #E8BE6A 70%, #F2EDE4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 200% auto;
        animation: gradientFlow 5s ease infinite;
        letter-spacing: -0.02em;
    }
    @keyframes gradientFlow {
        0%   { background-position: 0% center; }
        50%  { background-position: 100% center; }
        100% { background-position: 0% center; }
    }
    .hero-tagline {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.25rem;
        font-style: italic;
        font-weight: 300;
        color: var(--gold-light);
        margin-bottom: 1.2rem;
        opacity: 0.85;
    }
    .hero-bio {
        font-size: 1rem;
        color: var(--mist);
        line-height: 1.85;
        max-width: 520px;
        margin-bottom: 0.5rem;
    }

    /* ── CTA Buttons ── */
    .cta-primary > button {
        background: linear-gradient(135deg, #C9973A, #E8BE6A) !important;
        border: none !important;
        color: #080C18 !important;
        font-weight: 700 !important;
        letter-spacing: 0.1em !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 20px rgba(201,151,58,0.35) !important;
        transition: all 0.3s ease !important;
    }
    .cta-primary > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 30px rgba(201,151,58,0.5) !important;
        background: linear-gradient(135deg, #E8BE6A, #C9973A) !important;
    }
    .cta-secondary > button {
        background: transparent !important;
        border: 1px solid rgba(201,151,58,0.4) !important;
        color: var(--gold-light) !important;
        font-weight: 500 !important;
        letter-spacing: 0.1em !important;
        border-radius: 10px !important;
    }
    .cta-secondary > button:hover {
        background: rgba(201,151,58,0.08) !important;
        border-color: var(--gold) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 20px rgba(201,151,58,0.2) !important;
        color: var(--gold-light) !important;
    }

    /* ── Stat cards ── */
    .stat-card {
        background: linear-gradient(145deg, #131E30, #0F1829);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.5rem 1rem;
        text-align: center;
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
    }
    .stat-card::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0;
        width: 100%; height: 3px;
        background: linear-gradient(90deg, var(--gold), var(--teal));
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.4s ease;
    }
    .stat-card:hover {
        border-color: rgba(201,151,58,0.35);
        transform: translateY(-6px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.4), 0 0 20px rgba(201,151,58,0.1);
    }
    .stat-card:hover::after { transform: scaleX(1); }
    .stat-num {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.8rem;
        font-weight: 400;
        background: linear-gradient(135deg, #C9973A, #00C2D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        margin-bottom: 0.4rem;
    }
    .stat-lbl {
        font-size: 0.7rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--steel);
        font-weight: 500;
    }

    /* ── Section headers ── */
    .section-eyebrow {
        font-size: 0.68rem;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        color: var(--gold);
        font-weight: 600;
        margin-bottom: 0.3rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .section-eyebrow::after {
        content: '';
        flex: 1;
        max-width: 40px;
        height: 1px;
        background: linear-gradient(90deg, var(--gold), transparent);
    }
    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.4rem;
        font-weight: 300;
        color: var(--ivory);
        margin-bottom: 2rem;
        letter-spacing: -0.01em;
    }

    /* ── Project cards ── */
    .proj-card {
        background: linear-gradient(145deg, #131E30, #0F1829);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.6rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
    }
    .proj-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: radial-gradient(circle at top left, rgba(201,151,58,0.06), transparent 60%);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    .proj-card::after {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 3px;
        background: linear-gradient(90deg, var(--gold), var(--teal), var(--gold));
        background-size: 200% 100%;
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.4s ease;
        animation: shimmerBar 3s ease infinite;
    }
    @keyframes shimmerBar {
        0%   { background-position: 0% 0; }
        100% { background-position: 200% 0; }
    }
    .proj-card:hover {
        border-color: rgba(201,151,58,0.4);
        transform: translateY(-8px);
        box-shadow: 0 20px 50px rgba(0,0,0,0.5), 0 0 30px rgba(201,151,58,0.08);
    }
    .proj-card:hover::before { opacity: 1; }
    .proj-card:hover::after  { transform: scaleX(1); }

    /* ── Tech strip ── */
    .tech-pill {
        display: inline-block;
        background: rgba(0,194,212,0.08);
        border: 1px solid rgba(0,194,212,0.2);
        color: #00C2D4;
        font-family: 'DM Mono', monospace;
        font-size: 0.72rem;
        padding: 4px 12px;
        border-radius: 20px;
        margin: 3px 4px 3px 0;
        letter-spacing: 0.03em;
        transition: all 0.25s ease;
    }
    .tech-pill:hover {
        background: rgba(0,194,212,0.15);
        border-color: rgba(0,194,212,0.4);
        transform: translateY(-1px);
    }

    /* ── Gradient divider ── */
    .grad-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(201,151,58,0.3), rgba(0,194,212,0.2), transparent);
        margin: 2.5rem 0;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── HERO SECTION ──────────────────────────────────────────────────────────
    col_img, col_text = st.columns([1, 2.2], gap="large")

    with col_img:
        st.markdown(
            "<div style='display:flex;justify-content:center;"
            "align-items:center;height:100%;padding-top:1.5rem;'>"
            "<div class='avatar-ring'>"
            "<span style='filter:drop-shadow(0 0 12px rgba(201,151,58,0.5));'>👨‍💻</span>"
            "<div class='avatar-status'></div>"
            "</div></div>",
            unsafe_allow_html=True,
        )

    with col_text:
        st.markdown(
            "<div class='hero-eyebrow'>Data Science &amp; Analytics</div>"
            "<div class='hero-name-enhanced'>" + PERSONAL['name_first'] + "<br>" + PERSONAL['name_last'] + "</div>"
            "<div class='hero-tagline'>\"" + PERSONAL['tagline'] + "\"</div>"
            "<div class='hero-bio'>" + PERSONAL['intro'] + "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("<div style='height:1.8rem'></div>", unsafe_allow_html=True)

        b1, b2, b3 = st.columns([1.1, 1.1, 1.3], gap="small")
        with b1:
            st.markdown('<div class="cta-primary">', unsafe_allow_html=True)
            if st.button("⚡ View Projects", key="cta_projects", use_container_width=True):
                st.session_state.current_page = "Projects"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with b2:
            st.markdown('<div class="cta-secondary">', unsafe_allow_html=True)
            if st.button("✉ Contact Me", key="cta_contact", use_container_width=True):
                st.session_state.current_page = "Contact"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with b3:
            st.markdown(
                '<a href="' + PERSONAL["github"] + '" target="_blank" '
                'style="display:flex;align-items:center;gap:6px;padding:0.75rem 0.5rem;'
                'font-size:0.82rem;color:#607A94;text-decoration:none;'
                'transition:color 0.3s ease;">'
                '⭐ <span>GitHub Profile →</span></a>',
                unsafe_allow_html=True,
            )

    # ── STATS ─────────────────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:0.68rem;letter-spacing:0.22em;text-transform:uppercase;"
        "color:rgba(201,151,58,0.5);margin-bottom:1rem;font-weight:600;'>At a Glance</p>",
        unsafe_allow_html=True,
    )

    stat_cols = st.columns(len(STATS))
    colors = ["#C9973A", "#00C2D4", "#00C896", "#FF6B8A"]
    for col, (num, label), color in zip(stat_cols, STATS, colors):
        with col:
            st.markdown(
                "<div class='stat-card'>"
                "<div class='stat-num' style='background:linear-gradient(135deg,"
                + color + ",#E8BE6A);-webkit-background-clip:text;"
                "-webkit-text-fill-color:transparent;background-clip:text;'>"
                + num + "</div>"
                "<div class='stat-lbl'>" + label + "</div>"
                "</div>",
                unsafe_allow_html=True,
            )

    # ── FEATURED PROJECTS ─────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-eyebrow'>Featured Work</div>"
        "<div class='section-title'>Recent Projects</div>",
        unsafe_allow_html=True,
    )

    from components.data import PROJECTS
    proj_cols = st.columns(3, gap="large")
    card_accents = ["#C9973A", "#00C2D4", "#00C896"]

    for i, project in enumerate(PROJECTS[:3]):
        with proj_cols[i]:
            accent = card_accents[i % 3]
            tech_tags = "".join(
                '<span class="tech-pill">' + t + '</span>'
                for t in project["tech"][:3]
            )
            github_btn = (
                '<a href="' + project["github"] + '" target="_blank" '
                'style="flex:1;text-align:center;padding:0.55rem;'
                'background:rgba(201,151,58,0.08);border:1px solid rgba(201,151,58,0.25);'
                'border-radius:8px;color:#C9973A;text-decoration:none;font-size:0.8rem;">⭐ GitHub</a>'
            )
            demo_btn = (
                '<div style="flex:1;text-align:center;padding:0.55rem;'
                'background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);'
                'border-radius:8px;color:rgba(255,255,255,0.25);font-size:0.8rem;'
                'cursor:not-allowed;">No Demo</div>'
            )

            st.markdown(
                "<div class='proj-card'>"
                "<div style='font-size:2rem;margin-bottom:0.8rem;'>" + project['icon'] + "</div>"
                "<div style='font-size:1rem;font-weight:600;color:#F2EDE4;"
                "margin-bottom:0.2rem;'>" + project['title'] + "</div>"
                "<div style='font-size:0.68rem;color:" + accent + ";text-transform:uppercase;"
                "letter-spacing:0.1em;font-weight:600;margin-bottom:0.8rem;'>"
                + project['category'] + "</div>"
                "<p style='font-size:0.87rem;color:#607A94;line-height:1.65;"
                "flex-grow:1;margin-bottom:1.1rem;'>"
                + project['description'][:115] + "…</p>"
                "<div style='margin-bottom:1rem;display:flex;flex-wrap:wrap;'>" + tech_tags + "</div>"
                "<div style='display:flex;gap:0.7rem;margin-top:auto;'>"
                + github_btn + demo_btn +
                "</div></div>",
                unsafe_allow_html=True,
            )

    # ── TECH STACK ────────────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:0.68rem;letter-spacing:0.22em;text-transform:uppercase;"
        "color:rgba(201,151,58,0.5);margin-bottom:1.2rem;font-weight:600;'>Core Stack</p>",
        unsafe_allow_html=True,
    )

    tools = ["Python", "Pandas", "NumPy", "Seaborn", "Matplotlib",
             "Power BI", "DAX", "MySQL", "Git", "HTML/CSS"]
    tags = "".join(
        '<span style="display:inline-block;background:rgba(201,151,58,0.07);'
        'border:1px solid rgba(201,151,58,0.2);color:#A8C0D6;'
        'font-family:DM Mono,monospace;font-size:0.78rem;'
        'padding:5px 14px;border-radius:20px;margin:3px 5px 3px 0;">'
        + t + '</span>'
        for t in tools
    )
    st.markdown(
        "<div style='line-height:2.8;'>" + tags + "</div>",
        unsafe_allow_html=True,
    )