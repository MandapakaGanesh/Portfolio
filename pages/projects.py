"""
Projects page — Compact professional cards, user-friendly layout.
"""

import streamlit as st
from components.data import PROJECTS, CATEGORIES
from components.styles import section_header

GITHUB_LINKS = {
    "Avocado Ripeness Analysis (Training Capstone)": "https://github.com/MandapakaGanesh/Avocado-Ripeness-Analysis-Dashboard",
    "Abalone Data Analysis": "https://github.com/MandapakaGanesh",
    "Industrial Energy Insights Dashboard": "https://github.com/MandapakaGanesh",
    "Retail Store Analysis": "https://github.com/MandapakaGanesh/Retail-Stoer-Analysis",
}

CATEGORY_COLORS = {
    "Machine Learning":   ("#C9973A", "rgba(201,151,58,0.1)",  "rgba(201,151,58,0.25)"),
    "Data Analysis":      ("#00C2D4", "rgba(0,194,212,0.1)",   "rgba(0,194,212,0.25)"),
    "Data Visualization": ("#00C896", "rgba(0,200,150,0.1)",   "rgba(0,200,150,0.25)"),
    "Web Development":    ("#FF6B8A", "rgba(255,107,138,0.1)", "rgba(255,107,138,0.25)"),
}
DEFAULT_COLOR = ("#C9973A", "rgba(201,151,58,0.1)", "rgba(201,151,58,0.25)")


def render_projects():

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&display=swap');

    .proj-card-pro {
        background: linear-gradient(145deg, #0F1829, #0d1626);
        border: 1px solid rgba(201,151,58,0.12);
        border-radius: 16px;
        padding: 1.4rem;
        display: flex;
        flex-direction: column;
        position: relative;
        overflow: hidden;
        transition: all 0.35s cubic-bezier(0.4,0,0.2,1);
        margin-bottom: 1.2rem;
        min-height: 380px;
        max-height: 420px;
    }
    .proj-card-pro:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 40px rgba(0,0,0,0.5),
                    0 0 20px rgba(201,151,58,0.06);
        border-color: rgba(201,151,58,0.28);
    }
    .proj-icon-wrap {
        width: 44px; height: 44px;
        border-radius: 12px;
        display: flex; align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        margin-bottom: 0.75rem;
        flex-shrink: 0;
    }
    .cat-badge {
        display: inline-flex; align-items: center; gap: 4px;
        font-size: 0.6rem; font-weight: 600;
        letter-spacing: 0.1em; text-transform: uppercase;
        padding: 2px 8px; border-radius: 20px;
        margin-bottom: 0.5rem;
    }
    .proj-title {
        font-size: 0.95rem; font-weight: 600;
        color: #F2EDE4; margin-bottom: 0.5rem;
        line-height: 1.3;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .proj-desc {
        font-size: 0.82rem; color: #607A94;
        line-height: 1.6; margin-bottom: 0.8rem;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
        flex-grow: 1;
    }
    .tech-pill-pro {
        display: inline-block;
        background: rgba(0,194,212,0.07);
        border: 1px solid rgba(0,194,212,0.16);
        color: #607A94;
        font-family: 'DM Mono', monospace;
        font-size: 0.65rem; padding: 2px 8px;
        border-radius: 20px;
        margin: 2px 2px 2px 0;
    }
    .count-badge {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(201,151,58,0.08);
        border: 1px solid rgba(201,151,58,0.2);
        color: #C9973A; font-size: 0.75rem;
        padding: 4px 12px; border-radius: 20px; font-weight: 500;
    }
    .grad-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent,
            rgba(201,151,58,0.25), rgba(0,194,212,0.15), transparent);
        margin: 0.5rem 0 1.8rem; border: none;
    }
    .highlight-row {
        display: flex; align-items: flex-start;
        gap: 6px; font-size: 0.76rem;
        color: #A8C0D6; margin-bottom: 0.2rem;
        line-height: 1.4;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(section_header("Portfolio", "Projects"), unsafe_allow_html=True)

    # ── Filter + Count ────────────────────────────────────────────────────────
    filter_col, count_col = st.columns([2, 3])
    with filter_col:
        selected_cat = st.selectbox(
            "Filter", options=CATEGORIES,
            key="project_filter", label_visibility="collapsed",
        )
    filtered = (
        PROJECTS if selected_cat == "All"
        else [p for p in PROJECTS if p["category"] == selected_cat]
    )
    with count_col:
        st.markdown(
            "<div style='padding-top:0.4rem;'>"
            "<span class='count-badge'>📁 "
            + str(len(filtered))
            + " project" + ("s" if len(filtered) != 1 else "")
            + "</span></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)

    if not filtered:
        st.info("No projects found. Try a different category.")
        return

    # ── Cards ─────────────────────────────────────────────────────────────────
    cols = st.columns(3, gap="large")
    for i, project in enumerate(filtered):
        with cols[i % 3]:
            github_url = GITHUB_LINKS.get(project["title"], project["github"])
            color, bg, border = CATEGORY_COLORS.get(project["category"], DEFAULT_COLOR)

            # Max 3 tech tags to keep cards compact
            tech_tags = "".join(
                "<span class='tech-pill-pro'>" + t + "</span>"
                for t in project["tech"][:3]
            )

            # Only 1 highlight to save space
            highlight = (
                "<div class='highlight-row'>"
                "<span style='color:" + color + ";font-size:0.7rem;margin-top:1px;'>✦</span>"
                "<span>" + project["highlights"][0] + "</span>"
                "</div>"
                if project.get("highlights") else ""
            )

            github_btn = (
                '<a href="' + github_url + '" target="_blank" '
                'style="flex:1;text-align:center;padding:0.5rem;'
                'background:rgba(201,151,58,0.08);'
                'border:1px solid rgba(201,151,58,0.22);'
                'border-radius:8px;color:#C9973A;text-decoration:none;'
                'font-size:0.78rem;font-weight:500;">⭐ GitHub</a>'
            )
            demo_btn = (
                '<a href="' + project["demo"] + '" target="_blank" '
                'style="flex:1;text-align:center;padding:0.5rem;'
                'background:rgba(0,194,212,0.07);'
                'border:1px solid rgba(0,194,212,0.18);'
                'border-radius:8px;color:#00C2D4;text-decoration:none;'
                'font-size:0.78rem;font-weight:500;">🔗 Demo</a>'
                if project.get("demo") else
                '<div style="flex:1;text-align:center;padding:0.5rem;'
                'background:rgba(255,255,255,0.02);'
                'border:1px solid rgba(255,255,255,0.05);'
                'border-radius:8px;color:rgba(255,255,255,0.18);'
                'font-size:0.78rem;cursor:not-allowed;">No Demo</div>'
            )

            # Truncate description to ~100 chars for readability
            short_desc = (
                project["description"][:100] + "…"
                if len(project["description"]) > 100
                else project["description"]
            )

            card_html = (
                "<div class='proj-card-pro'"
                " style='border-top:3px solid " + color + ";'>"

                # Icon box
                "<div class='proj-icon-wrap'"
                " style='background:" + bg + ";"
                "border:1px solid " + border + ";'>"
                + project["icon"] + "</div>"

                # Category badge
                "<div class='cat-badge'"
                " style='background:" + bg + ";"
                "border:1px solid " + border + ";"
                "color:" + color + ";'>"
                "<span style='width:4px;height:4px;background:" + color + ";"
                "border-radius:50%;display:inline-block;'></span>"
                + project["category"] + "</div>"

                # Title (clamps to 2 lines)
                "<div class='proj-title'>" + project["title"] + "</div>"

                # Description (clamps to 3 lines)
                "<div class='proj-desc'>" + short_desc + "</div>"

                # Top highlight
                "<div style='margin-bottom:0.7rem;'>" + highlight + "</div>"

                # Tech tags
                "<div style='margin-bottom:0.9rem;"
                "display:flex;flex-wrap:wrap;'>" + tech_tags + "</div>"

                # Action buttons
                "<div style='display:flex;gap:0.6rem;margin-top:auto;'>"
                + github_btn + demo_btn + "</div>"

                "</div>"
            )

            st.markdown(card_html, unsafe_allow_html=True)