"""
Contact page — Enhanced professional design with rich color palette.
"""

import streamlit as st
from components.data import PERSONAL
from components.styles import section_header


def render_contact():

    st.markdown("""
    <style>
    .contact-card-pro {
        background: linear-gradient(145deg, #0F1829, #0d1626);
        border: 1px solid rgba(201,151,58,0.12);
        border-radius: 16px;
        padding: 1.8rem 1.2rem;
        text-align: center;
        transition: all 0.35s cubic-bezier(0.4,0,0.2,1);
        position: relative; overflow: hidden;
        text-decoration: none; display: block;
        height: 100%;
    }
    .contact-card-pro::after {
        content: '';
        position: absolute; bottom: 0; left: 0;
        width: 100%; height: 3px;
        transform: scaleX(0); transform-origin: center;
        transition: transform 0.35s ease;
    }
    .contact-card-pro:hover {
        transform: translateY(-7px);
        box-shadow: 0 16px 40px rgba(0,0,0,0.45);
        border-color: rgba(201,151,58,0.3);
    }
    .contact-card-pro:hover::after { transform: scaleX(1); }

    .contact-icon-wrap {
        width: 56px; height: 56px;
        border-radius: 16px;
        display: flex; align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        margin: 0 auto 1rem;
        transition: transform 0.35s ease;
    }
    .contact-card-pro:hover .contact-icon-wrap {
        transform: scale(1.1) rotate(-5deg);
    }

    .avail-card {
        background: linear-gradient(145deg, #0F1829, #0d1626);
        border: 1px solid rgba(0,200,150,0.2);
        border-left: 4px solid #00C896;
        border-radius: 0 14px 14px 0;
        padding: 1.5rem 1.8rem;
        max-width: 520px;
    }

    .form-card {
        background: linear-gradient(145deg, #0F1829, #0d1626);
        border: 1px solid rgba(201,151,58,0.12);
        border-radius: 16px;
        padding: 2rem;
    }

    .grad-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent,
            rgba(201,151,58,0.25), rgba(0,194,212,0.15), transparent);
        margin: 2rem 0; border: none;
    }
    .section-eyebrow {
        font-size: 0.65rem; letter-spacing: 0.25em;
        text-transform: uppercase; color: #C9973A;
        font-weight: 600; margin-bottom: 0.3rem;
    }
    .section-title-sm {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem; font-weight: 300;
        color: #F2EDE4; margin-bottom: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(section_header("Get in Touch", "Contact"), unsafe_allow_html=True)

    # ── Intro ─────────────────────────────────────────────────────────────────
    st.markdown(
        "<p style='color:#607A94;font-size:0.95rem;line-height:1.8;"
        "max-width:560px;margin-bottom:2rem;'>"
        "I'm always open to discussing data science opportunities, research "
        "collaborations, or just talking about interesting datasets. "
        "Feel free to reach out through any of the channels below."
        "</p>",
        unsafe_allow_html=True,
    )

    # ── Contact cards ─────────────────────────────────────────────────────────
    contact_items = [
        ("✉️",  "Email",    PERSONAL["email"],
         f'mailto:{PERSONAL["email"]}',
         "#C9973A", "rgba(201,151,58,0.1)", "rgba(201,151,58,0.25)",
         "linear-gradient(90deg,#C9973A,#E8BE6A)"),
        ("💼",  "LinkedIn", "linkedin.com/in/mandapaka-ganesh",
         PERSONAL["linkedin"],
         "#00C2D4", "rgba(0,194,212,0.1)", "rgba(0,194,212,0.25)",
         "linear-gradient(90deg,#00C2D4,#48CAE4)"),
        ("⭐",  "GitHub",   "github.com/MandapakaGanesh",
         PERSONAL["github"],
         "#00C896", "rgba(0,200,150,0.1)", "rgba(0,200,150,0.25)",
         "linear-gradient(90deg,#00C896,#34D399)"),
        ("📍",  "Location", PERSONAL["location"],
         None,
         "#FF6B8A", "rgba(255,107,138,0.1)", "rgba(255,107,138,0.25)",
         "linear-gradient(90deg,#FF6B8A,#FF8E8E)"),
    ]

    c1, c2, c3, c4 = st.columns(4, gap="medium")
    for col, (icon, label, value, url, color, bg, border, grad) in zip(
        [c1, c2, c3, c4], contact_items
    ):
        with col:
            href  = url if url else "#"
            target = '_blank' if url and not url.startswith('mailto') else '_self'
            st.markdown(
                '<a href="' + href + '" target="' + target + '"'
                ' style="text-decoration:none;display:block;">'
                "<div class='contact-card-pro'"
                " style='border-top:3px solid " + color + ";'>"
                "<div class='contact-icon-wrap'"
                " style='background:" + bg + ";border:1px solid " + border + ";'>"
                + icon + "</div>"
                "<div style='font-size:0.65rem;letter-spacing:0.15em;"
                "text-transform:uppercase;font-weight:600;color:" + color + ";"
                "margin-bottom:0.4rem;'>" + label + "</div>"
                "<div style='font-size:0.82rem;color:#A8C0D6;"
                "word-break:break-word;line-height:1.4;'>" + value + "</div>"
                "</div></a>",
                unsafe_allow_html=True,
            )

    # ── Contact form ──────────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-eyebrow'>Send a Message</div>"
        "<div class='section-title-sm'>Direct Message</div>",
        unsafe_allow_html=True,
    )

    form_col, _ = st.columns([2, 1])
    with form_col:
        st.markdown("<div class='form-card'>", unsafe_allow_html=True)

        name_col, email_col = st.columns(2)
        with name_col:
            name_val = st.text_input("Your Name", placeholder="Jane Smith")
        with email_col:
            email_val = st.text_input("Your Email", placeholder="jane@example.com")

        subject_val = st.text_input(
            "Subject",
            placeholder="Data Science Opportunity / Collaboration / Other"
        )
        message_val = st.text_area(
            "Message",
            placeholder=f"Hi {PERSONAL['name'].split()[0]}, I'd love to discuss…",
            height=140,
        )

        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

        if st.button("Send Message →", key="send_msg"):
            if name_val and email_val and message_val:
                st.success(
                    f"✅ Message received! Thanks, {name_val.split()[0]}. "
                    f"I'll reply to {email_val} within 24 hours."
                )
                st.balloons()
            else:
                st.warning("Please fill in your name, email, and message.")

        st.markdown("</div>", unsafe_allow_html=True)

    # ── Availability ──────────────────────────────────────────────────────────
    st.markdown("<div class='grad-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='avail-card'>"
        "<div style='display:flex;align-items:center;gap:0.75rem;margin-bottom:0.8rem;'>"
        "<span style='font-size:1.4rem;'>🗓️</span>"
        "<div>"
        "<div style='font-size:0.95rem;font-weight:600;color:#F2EDE4;'>Availability</div>"
        "<div style='font-size:0.7rem;color:#607A94;letter-spacing:0.08em;'>Current Status</div>"
        "</div></div>"
        "<p style='color:#607A94;font-size:0.87rem;line-height:1.75;margin:0;'>"
        "I'm currently available for "
        "<strong style='color:#00C896;'>internships</strong>, "
        "<strong style='color:#00C896;'>part-time data roles</strong>, and "
        "<strong style='color:#00C896;'>research collaborations</strong> "
        "starting Summer 2025. Especially interested in "
        "healthcare analytics and fintech domains."
        "</p></div>",
        unsafe_allow_html=True,
    )