"""
Skills Dashboard — Enhanced professional design with custom progress bars.
"""

import streamlit as st
from components.data import SKILLS
from components.styles import section_header

CATEGORY_COLORS = {
    "Programming":       ("#C9973A", "rgba(201,151,58,0.12)",  "rgba(201,151,58,0.25)"),
    "Data Analysis":     ("#00C2D4", "rgba(0,194,212,0.12)",   "rgba(0,194,212,0.25)"),
    "Tools & Platforms": ("#00C896", "rgba(0,200,150,0.12)",   "rgba(0,200,150,0.25)"),
    "Visualization":     ("#FF6B8A", "rgba(255,107,138,0.12)", "rgba(255,107,138,0.25)"),
    "Machine Learning":  ("#A78BFA", "rgba(167,139,250,0.12)", "rgba(167,139,250,0.25)"),
}
DEFAULT_COLOR = ("#C9973A", "rgba(201,151,58,0.12)", "rgba(201,151,58,0.25)")

CATEGORY_ICONS = {
    "Programming":       "🐍",
    "Data Analysis":     "📊",
    "Tools & Platforms": "🛠️",
    "Visualization":     "🎨",
    "Machine Learning":  "🤖",
}

def _level(pct):
    if pct >= 90: return "Expert",     "#00C896"
    if pct >= 75: return "Advanced",   "#00C2D4"
    if pct >= 60: return "Proficient", "#C9973A"
    return               "Learning",   "#FF6B8A"


def render_skills():

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&display=swap');

    .skill-card {
        background: linear-gradient(145deg, #0F1829, #0d1626);
        border: 1px solid rgba(201,151,58,0.12);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        transition: all 0.35s ease;
    }
    .skill-card:hover {
        border-color: rgba(201,151,58,0.25);
        box-shadow: 0 12px 35px rgba(0,0,0,0.4);
        transform: translateY(-3px);
    }
    .skill-card-header {
        display: flex; align-items: center;
        gap: 0.75rem; margin-bottom: 1.3rem;
        padding-bottom: 0.9rem;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .skill-icon-box {
        width: 42px; height: 42px;
        border-radius: 11px;
        display: flex; align-items: center;
        justify-content: center; font-size: 1.3rem;
        flex-shrink: 0;
    }
    .skill-cat-name {
        font-size: 0.95rem; font-weight: 600;
        color: #F2EDE4; margin-bottom: 0.1rem;
    }
    .skill-cat-sub {
        font-size: 0.68rem; color: #607A94;
        letter-spacing: 0.06em;
    }
    .skill-avg-badge {
        margin-left: auto;
        font-family: 'DM Mono', monospace;
        font-size: 1.3rem; font-weight: 500;
    }

    /* Custom progress bar */
    .skill-row {
        margin-bottom: 0.85rem;
    }
    .skill-row-top {
        display: flex; justify-content: space-between;
        align-items: center; margin-bottom: 0.35rem;
    }
    .skill-row-name {
        font-size: 0.83rem; color: #A8C0D6; font-weight: 500;
    }
    .skill-row-right {
        display: flex; align-items: center; gap: 8px;
    }
    .skill-pct {
        font-family: 'DM Mono', monospace;
        font-size: 0.75rem; color: #607A94;
    }
    .skill-level-badge {
        font-size: 0.6rem; font-weight: 600;
        letter-spacing: 0.08em; text-transform: uppercase;
        padding: 2px 7px; border-radius: 20px;
    }
    .skill-bar-track {
        height: 6px; border-radius: 10px;
        background: rgba(255,255,255,0.05);
        overflow: hidden; position: relative;
    }
    .skill-bar-fill {
        height: 100%; border-radius: 10px;
        position: relative; overflow: hidden;
        transition: width 1.2s ease;
    }
    .skill-bar-fill::after {
        content: '';
        position: absolute; top: 0; left: -100%;
        width: 100%; height: 100%;
        background: linear-gradient(90deg,
            transparent, rgba(255,255,255,0.3), transparent);
        animation: shimmer 2.5s ease infinite;
    }
    @keyframes shimmer {
        0%   { left: -100%; }
        100% { left: 200%; }
    }

    /* Overview stat cards */
    .overview-card {
        background: linear-gradient(145deg, #0F1829, #0d1626);
        border: 1px solid rgba(201,151,58,0.12);
        border-radius: 14px;
        padding: 1.3rem 1rem;
        text-align: center;
        transition: all 0.35s ease;
        position: relative; overflow: hidden;
    }
    .overview-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.4);
    }
    .overview-card::after {
        content: '';
        position: absolute; bottom: 0; left: 0;
        width: 100%; height: 3px;
        transform: scaleX(0); transform-origin: left;
        transition: transform 0.35s ease;
    }
    .overview-card:hover::after { transform: scaleX(1); }
    .overview-num {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.5rem; font-weight: 300; line-height: 1;
        margin-bottom: 0.3rem;
    }
    .overview-label {
        font-size: 0.68rem; letter-spacing: 0.12em;
        text-transform: uppercase; color: #607A94;
        font-weight: 500;
    }

    .grad-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent,
            rgba(201,151,58,0.25), rgba(0,194,212,0.15), transparent);
        margin: 2rem 0; border: none;
    }

    /* Legend */
    .legend-item {
        display: flex; align-items: center; gap: 8px;
        font-size: 0.78rem; color: #607A94;
    }
    .legend-dot {
        width: 10px; height: 10px;
        border-radius: 50%; flex-shrink: 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── Header ────────────────────────────────────────────────────────────────
    st.markdown(section_header("Proficiency", "Skills Dashboard"),
                unsafe_allow_html=True)

    # ── Summary note ──────────────────────────────────────────────────────────
    st.markdown(
        "<div style='background:linear-gradient(145deg,#0F1829,#0d1626);"
        "border:1px solid rgba(201,151,58,0.12);border-left:3px solid #C9973A;"
        "border-radius:0 12px 12px 0;padding:1rem 1.4rem;margin-bottom:1.8rem;'>"
        "<p style='font-size:0.85rem;color:#607A94;margin:0;line-height:1.7;'>"
        "Proficiency ratings are <strong style='color:#A8C0D6;'>self-assessed</strong> "
        "based on project experience, coursework, and hands-on practice. "
        "They reflect practical working ability, not theoretical perfection."
        "</p></div>",
        unsafe_allow_html=True,
    )

    # ── Overview cards ────────────────────────────────────────────────────────
    ov_cols = st.columns(len(SKILLS), gap="small")
    for col, (cat, skills_list) in zip(ov_cols, SKILLS.items()):
        avg  = sum(p for _, p in skills_list) // len(skills_list)
        icon = CATEGORY_ICONS.get(cat, "📌")
        color, bg, border = CATEGORY_COLORS.get(cat, DEFAULT_COLOR)
        with col:
            st.markdown(
                "<div class='overview-card'"
                " style='border-top:3px solid " + color + ";'>"
                "<div style='font-size:1.6rem;margin-bottom:0.5rem;'>" + icon + "</div>"
                "<div class='overview-num' style='color:" + color + ";'>"
                + str(avg) + "%</div>"
                "<div class='overview-label'>" + cat + "</div>"
                "</div>",
                unsafe_allow_html=True,
            )

    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)

    # ── Skill bars (2 columns) ────────────────────────────────────────────────
    cat_items = list(SKILLS.items())
    for row_start in range(0, len(cat_items), 2):
        row_cats = cat_items[row_start:row_start + 2]
        cols = st.columns(2, gap="large")

        for col, (category, skills_list) in zip(cols, row_cats):
            with col:
                color, bg, border = CATEGORY_COLORS.get(category, DEFAULT_COLOR)
                icon = CATEGORY_ICONS.get(category, "📌")
                avg  = sum(p for _, p in skills_list) // len(skills_list)

                # Card header
                st.markdown(
                    "<div class='skill-card'>"
                    "<div class='skill-card-header'>"
                    "<div class='skill-icon-box'"
                    " style='background:" + bg + ";border:1px solid " + border + ";'>"
                    + icon + "</div>"
                    "<div>"
                    "<div class='skill-cat-name'>" + category + "</div>"
                    "<div class='skill-cat-sub'>" + str(len(skills_list)) + " skills tracked</div>"
                    "</div>"
                    "<div class='skill-avg-badge' style='color:" + color + ";'>"
                    + str(avg) + "%</div>"
                    "</div>",
                    unsafe_allow_html=True,
                )

                # Individual skill bars
                for skill_name, pct in sorted(skills_list, key=lambda x: x[1], reverse=True):
                    level_label, level_color = _level(pct)
                    bar_html = (
                        "<div class='skill-row'>"
                        "<div class='skill-row-top'>"
                        "<span class='skill-row-name'>" + skill_name + "</span>"
                        "<div class='skill-row-right'>"
                        "<span class='skill-pct'>" + str(pct) + "%</span>"
                        "<span class='skill-level-badge'"
                        " style='background:" + level_color + "22;"
                        "border:1px solid " + level_color + "44;"
                        "color:" + level_color + ";'>"
                        + level_label + "</span>"
                        "</div></div>"
                        "<div class='skill-bar-track'>"
                        "<div class='skill-bar-fill'"
                        " style='width:" + str(pct) + "%;"
                        "background:linear-gradient(90deg," + color + "," + level_color + ");'>"
                        "</div></div></div>"
                    )
                    st.markdown(bar_html, unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

    # ── Legend ────────────────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:0.65rem;letter-spacing:0.22em;text-transform:uppercase;"
        "color:rgba(201,151,58,0.6);margin-bottom:0.8rem;font-weight:600;'>Proficiency Legend</p>"
        "<div style='display:flex;gap:1.8rem;flex-wrap:wrap;'>"
        "<div class='legend-item'>"
        "<div class='legend-dot' style='background:#00C896;box-shadow:0 0 6px #00C896;'></div>"
        "90–100 · Expert</div>"
        "<div class='legend-item'>"
        "<div class='legend-dot' style='background:#00C2D4;box-shadow:0 0 6px #00C2D4;'></div>"
        "75–89 · Advanced</div>"
        "<div class='legend-item'>"
        "<div class='legend-dot' style='background:#C9973A;box-shadow:0 0 6px #C9973A;'></div>"
        "60–74 · Proficient</div>"
        "<div class='legend-item'>"
        "<div class='legend-dot' style='background:#FF6B8A;box-shadow:0 0 6px #FF6B8A;'></div>"
        "&lt;60 · Learning</div>"
        "</div>",
        unsafe_allow_html=True,
    )