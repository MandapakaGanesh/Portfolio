"""
Custom CSS styles for the portfolio application.
Defines the global styling, color palette, typography, and component styles.
"""

def load_css():
    """Returns the main CSS string for the entire portfolio."""
    return """
    <style>
    /* =============================
       IMPORT GOOGLE FONTS
       ============================= */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

    /* =============================
       CSS VARIABLES — COLOR PALETTE
       ============================= */
    :root {
        --navy:       #0A0E1A;
        --navy-mid:   #162032;
        --navy-light: #1F2F45;
        --slate:      #5D7A99;
        --steel:      #8BA3C7;
        --mist:       #C5D8E6;
        --ivory:      #F8F5F0;
        --white:      #FFFFFF;

        --gold:       #D4AF37;
        --gold-light: #F4D03F;
        --gold-gradient: linear-gradient(135deg, #D4AF37 0%, #F4D03F 100%);

        --teal:       #00B4D8;
        --teal-light: #48CAE4;
        --purple:     #9D4EDD;
        --purple-light: #C77DFF;
        --coral:      #FF6B6B;
        --coral-light: #FF8E8E;
        --emerald:    #10B981;
        --emerald-light: #34D399;

        --success:    #10B981;
        --success-glow: rgba(16, 185, 129, 0.4);
        --info:       #3B82F6;
        --warning:    #F59E0B;
        --error:      #EF4444;

        --border:     rgba(197, 216, 230, 0.25);
        --card-bg:    rgba(22, 32, 50, 0.75);
        --card-hover: rgba(31, 47, 69, 0.85);

        --shadow:     0 10px 40px rgba(0, 0, 0, 0.4);
        --shadow-sm:  0 4px 16px rgba(0, 0, 0, 0.2);
        --shadow-lg:  0 20px 60px rgba(0, 0, 0, 0.5);
        --glow-gold:  0 0 20px rgba(212, 175, 55, 0.5);
        --glow-teal:  0 0 20px rgba(0, 180, 216, 0.4);
        --glow-purple: 0 0 20px rgba(157, 78, 221, 0.4);
    }

    /* =============================
       GLOBAL RESET & BASE
       ============================= */
    .stApp {
        background-color: #080C18 !important;
        font-family: 'DM Sans', sans-serif !important;
        color: var(--ivory) !important;
        overflow-x: hidden;
    }

    /* =============================
       HIDE STREAMLIT UI — SAFE VERSION
       Keeps sidebar toggle button visible
       ============================= */

    /* Hide menu, footer, deploy button */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stDeployButton { display: none; }

    /* Hide toolbar content but NOT the sidebar toggle */
    [data-testid="stToolbar"]      { display: none !important; }
    [data-testid="stDecoration"]   { display: none !important; }
    [data-testid="stStatusWidget"] { display: none !important; }

    /* ✅ DO NOT hide stHeader or .stApp > header — they contain the sidebar button */

    /* Hide auto-generated sidebar page nav (pages/ folder duplicates) */
    [data-testid="stSidebarNav"] { display: none !important; }

    /* Force sidebar toggle button to always show */
    [data-testid="collapsedControl"] { display: flex !important; }
    button[kind="header"]            { display: flex !important; }

    /* =============================
       ANIMATIONS
       ============================= */
    html { scroll-behavior: smooth; }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50%      { transform: translateY(-10px); }
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50%      { opacity: 0.5; }
    }
    @keyframes shimmer {
        0%   { background-position: -1000px 0; }
        100% { background-position:  1000px 0; }
    }
    @keyframes gradientShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes spin {
        0%   { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes floatCard {
        0%, 100% { transform: translateY(0px); }
        50%      { transform: translateY(-5px); }
    }

    /* =============================
       SIDEBAR STYLING
       ============================= */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--navy-mid) 0%, var(--navy) 100%) !important;
        border-right: 1px solid rgba(201, 169, 110, 0.3) !important;
        padding-top: 0 !important;
        box-shadow: 5px 0 20px rgba(0, 0, 0, 0.4);
    }

    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: var(--gold) !important;
        font-family: 'Cormorant Garamond', serif !important;
    }

    section[data-testid="stSidebar"] .stMarkdown p {
        color: var(--mist) !important;
        font-size: 0.8rem !important;
        line-height: 1.6 !important;
    }

    section[data-testid="stSidebar"] .stRadio > label {
        color: var(--mist) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
    }

    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        gap: 4px !important;
        display: flex !important;
        flex-direction: column !important;
    }

    section[data-testid="stSidebar"] .stRadio div[role="radio"] {
        background: transparent !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        margin-bottom: 4px !important;
        position: relative !important;
        overflow: hidden !important;
    }

    section[data-testid="stSidebar"] .stRadio div[role="radio"]:hover {
        background: rgba(201, 169, 110, 0.1) !important;
        transform: translateX(5px) !important;
        border-left: 3px solid var(--gold) !important;
    }

    section[data-testid="stSidebar"] .stRadio div[role="radio"][aria-selected="true"] {
        background: linear-gradient(90deg, rgba(201, 169, 110, 0.2), transparent) !important;
        border-left: 3px solid var(--gold) !important;
        color: var(--gold) !important;
        font-weight: 600 !important;
    }

    section[data-testid="stSidebar"] .stRadio div[role="radio"][aria-selected="true"]::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: radial-gradient(circle at center, rgba(201, 169, 110, 0.1), transparent);
        z-index: -1;
    }

    /* =============================
       MAIN CONTENT AREA
       ============================= */
    .main .block-container {
        padding: 1.5rem 2rem 4rem 2rem !important;
        max-width: 1100px !important;
        margin: 0 auto !important;
    }

    /* stVerticalBlock rule removed */

    /* =============================
       TYPOGRAPHY
       ============================= */
    h1 {
        font-family: 'Cormorant Garamond', serif !important;
        font-weight: 300 !important;
        letter-spacing: -0.02em !important;
        color: var(--white) !important;
        line-height: 1.1 !important;
    }
    h2 {
        font-family: 'Cormorant Garamond', serif !important;
        font-weight: 400 !important;
        color: var(--ivory) !important;
    }
    h3, h4 {
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        color: var(--ivory) !important;
    }
    p, li {
        font-family: 'DM Sans', sans-serif !important;
        color: var(--mist) !important;
        line-height: 1.75 !important;
    }
    code {
        font-family: 'DM Mono', monospace !important;
        background: var(--navy-light) !important;
        color: var(--gold) !important;
        padding: 2px 6px !important;
        border-radius: 4px !important;
        font-size: 0.85em !important;
    }

    /* =============================
       SECTION HEADERS
       ============================= */
    .section-header {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.8rem;
        font-weight: 300;
        color: var(--white);
        margin-bottom: 0.25rem;
        letter-spacing: -0.02em;
    }
    .section-subheader {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.8rem;
        font-weight: 500;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--gold);
        margin-bottom: 0.5rem;
    }
    .divider {
        height: 1px;
        background: linear-gradient(90deg, var(--gold) 0%, transparent 60%);
        margin: 1.5rem 0 2.5rem 0;
        border: none;
    }

    /* =============================
       CARD COMPONENT
       ============================= */
    .card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(15px);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow);
    }
    .card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 4px;
        background: linear-gradient(90deg, var(--gold), var(--teal), var(--purple), var(--gold));
        opacity: 0;
        transition: opacity 0.5s ease;
        background-size: 300% 100%;
    }
    .card::after {
        content: '';
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: radial-gradient(circle, rgba(212,175,55,0.08) 0%, rgba(0,180,216,0.05) 50%, transparent 70%);
        opacity: 0;
        transition: opacity 0.5s ease;
        pointer-events: none;
    }
    .card:hover {
        border-color: rgba(212, 175, 55, 0.6);
        transform: translateY(-8px) scale(1.03);
        box-shadow: var(--shadow-lg), var(--glow-gold);
        background: var(--card-hover);
    }
    .card:hover::before { opacity: 1; }
    .card:hover::after  { opacity: 1; }

    .card-title {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--white);
        margin-bottom: 0.5rem;
    }
    .card-subtitle {
        font-size: 0.78rem;
        color: var(--gold);
        letter-spacing: 0.1em;
        text-transform: uppercase;
        font-weight: 500;
        margin-bottom: 0.75rem;
    }
    .card-text {
        font-size: 0.9rem;
        color: var(--steel);
        line-height: 1.7;
    }

    /* =============================
       TAG / BADGE
       ============================= */
    .tag {
        display: inline-block;
        background: rgba(201, 169, 110, 0.12);
        border: 1px solid rgba(201, 169, 110, 0.3);
        color: var(--gold-light);
        font-family: 'DM Mono', monospace;
        font-size: 0.72rem;
        padding: 3px 10px;
        border-radius: 20px;
        margin: 3px 3px 3px 0;
        letter-spacing: 0.03em;
    }
    .tag-blue {
        background: rgba(74, 98, 128, 0.2);
        border-color: rgba(74, 98, 128, 0.4);
        color: var(--mist);
    }

    /* =============================
       BUTTONS
       ============================= */
    .stButton > button {
        background: linear-gradient(135deg, rgba(212,175,55,0.1), rgba(0,180,216,0.1)) !important;
        border: 2px solid var(--gold) !important;
        color: var(--gold) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        padding: 0.8rem 2.2rem !important;
        border-radius: 10px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative !important;
        overflow: hidden !important;
        z-index: 1 !important;
        backdrop-filter: blur(10px) !important;
    }
    .stButton > button::before { display: none !important; }
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--gold), var(--teal)) !important;
        color: var(--navy) !important;
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 10px 35px rgba(212,175,55,0.5), 0 0 20px rgba(0,180,216,0.3) !important;
        border-color: var(--gold-light) !important;
    }
    .stButton > button:disabled,
    .stButton > button[disabled] {
        background: rgba(27,43,59,0.8) !important;
        border: 1px solid rgba(184,205,217,0.2) !important;
        color: #B8CDD9 !important;
        border-radius: 10px !important;
        font-size: 0.82rem !important;
        font-weight: 400 !important;
        letter-spacing: 0.03em !important;
        text-transform: none !important;
        cursor: default !important;
        opacity: 1 !important;
        width: 100% !important;
        padding: 0.6rem 0.5rem !important;
    }
    .stButton > button:disabled:hover,
    .stButton > button[disabled]:hover {
        background: rgba(27,43,59,0.8) !important;
        transform: none !important;
        box-shadow: none !important;
    }

    /* =============================
       PROGRESS BARS
       ============================= */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--gold), var(--gold-light)) !important;
        border-radius: 4px !important;
        box-shadow: 0 0 10px rgba(201,169,110,0.5) !important;
    }
    .stProgress > div > div {
        background: var(--navy-light) !important;
        border-radius: 4px !important;
        height: 8px !important;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.3) !important;
    }

    /* =============================
       METRICS
       ============================= */
    div[data-testid="metric-container"] {
        background: var(--card-bg) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        padding: 1.5rem 1.8rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px) scale(1.05) !important;
        border-color: rgba(201,169,110,0.4) !important;
        box-shadow: 0 8px 25px rgba(201,169,110,0.2) !important;
    }
    div[data-testid="metric-container"] label {
        color: var(--steel) !important;
        font-size: 0.75rem !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
    }
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: var(--white) !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 2.2rem !important;
    }

    /* =============================
       FORM INPUTS
       ============================= */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--navy-mid) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: var(--ivory) !important;
        font-family: 'DM Sans', sans-serif !important;
        padding: 0.75rem 1rem !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--gold) !important;
        box-shadow: 0 0 0 2px rgba(201,169,110,0.15) !important;
    }
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label {
        color: var(--steel) !important;
        font-size: 0.8rem !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        font-weight: 500 !important;
    }
    .stSelectbox > div > div {
        background: var(--navy-mid) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: var(--ivory) !important;
    }

    /* =============================
       MISC
       ============================= */
    hr {
        border: none !important;
        border-top: 1px solid var(--border) !important;
        margin: 2rem 0 !important;
    }
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--navy); }
    ::-webkit-scrollbar-thumb { background: var(--navy-light); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--slate); }

    a { color: var(--gold) !important; text-decoration: none !important; }
    a:hover { color: var(--gold-light) !important; text-decoration: underline !important; }

    /* =============================
       SIDEBAR PROFILE
       ============================= */
    .sidebar-profile {
        text-align: center;
        padding: 2rem 1rem 1.5rem 1rem;
        border-bottom: 1px solid var(--border);
        margin-bottom: 1.5rem;
    }
    .sidebar-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.4rem;
        font-weight: 400;
        color: var(--white);
        margin: 0.75rem 0 0.25rem 0;
        line-height: 1.2;
    }
    .sidebar-title {
        font-size: 0.72rem;
        color: var(--gold);
        letter-spacing: 0.15em;
        text-transform: uppercase;
        font-weight: 500;
    }
    .sidebar-status {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(76,175,130,0.12);
        border: 1px solid rgba(76,175,130,0.3);
        color: #4CAF82;
        font-size: 0.7rem;
        padding: 4px 12px;
        border-radius: 20px;
        margin-top: 0.75rem;
        font-weight: 500;
        letter-spacing: 0.05em;
    }

    /* =============================
       HOME HERO
       ============================= */
    .hero-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 5rem;
        font-weight: 400;
        background: linear-gradient(135deg, #F8F5F0 0%, #D4AF37 50%, #F4D03F 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
        line-height: 1.1;
        margin-bottom: 0.5rem;
        filter: drop-shadow(0 0 30px rgba(212,175,55,0.3));
        animation: gradientShift 5s ease infinite;
        background-size: 200% auto;
    }
    .hero-title {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.85rem;
        font-weight: 500;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--gold);
        margin-bottom: 1.5rem;
    }
    .hero-intro {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.05rem;
        color: var(--steel);
        line-height: 1.8;
        max-width: 560px;
    }

    /* =============================
       CONTACT CARD
       ============================= */
    .contact-card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 2rem 1.5rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .contact-card:hover {
        border-color: rgba(201,169,110,0.5);
        transform: translateY(-8px) scale(1.05);
        box-shadow: 0 12px 40px rgba(201,169,110,0.2), 0 0 30px rgba(201,169,110,0.1);
    }

    /* =============================
       SKILL BAR LABEL
       ============================= */
    .skill-label {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 6px;
    }
    .skill-name {
        font-size: 0.85rem;
        color: var(--mist);
        font-weight: 500;
    }
    .skill-pct {
        font-family: 'DM Mono', monospace;
        font-size: 0.78rem;
        color: var(--gold);
    }

    /* =============================
       TIMELINE
       ============================= */
    .timeline-item {
        border-left: 3px solid var(--gold);
        padding-left: 1.75rem;
        margin-bottom: 2.5rem;
        position: relative;
        transition: all 0.3s ease;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px; top: 6px;
        width: 14px; height: 14px;
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        border-radius: 50%;
        box-shadow: 0 0 15px rgba(201,169,110,0.6);
        animation: pulse 2s ease-in-out infinite;
    }
    .timeline-item:hover { transform: translateX(5px); }
    .timeline-year {
        font-family: 'DM Mono', monospace;
        font-size: 0.75rem;
        color: var(--gold);
        letter-spacing: 0.1em;
        margin-bottom: 0.3rem;
    }
    .timeline-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: var(--white);
        margin-bottom: 0.2rem;
    }
    .timeline-sub {
        font-size: 0.85rem;
        color: var(--steel);
    }

    /* =============================
       STAT BOX
       ============================= */
    .stat-box {
        background: linear-gradient(135deg, rgba(22,32,50,0.8), rgba(31,47,69,0.9)) !important;
        border: 2px solid rgba(212,175,55,0.3) !important;
        border-radius: 18px !important;
        padding: 1.8rem 1.2rem !important;
        text-align: center;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow), 0 0 20px rgba(212,175,55,0.1) !important;
        backdrop-filter: blur(15px) !important;
    }
    .stat-box:hover {
        transform: translateY(-8px) scale(1.08) !important;
        border-color: rgba(212,175,55,0.6) !important;
        box-shadow: var(--shadow-lg), var(--glow-gold) !important;
    }
    .stat-number {
        font-family: 'Cormorant Garamond', serif;
        font-size: 3rem;
        font-weight: 400;
        background: linear-gradient(135deg, var(--gold), var(--teal-light), var(--gold-light));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        filter: drop-shadow(0 0 10px rgba(212,175,55,0.3));
    }
    .stat-label {
        font-size: 0.72rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--steel);
        margin-top: 0.3rem;
    }

    /* =============================
       PROJECT CARD
       ============================= */
    .project-card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 2rem;
        height: 100%;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .project-card::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0;
        width: 100%; height: 4px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light), var(--gold));
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .project-card > * { position: relative; z-index: 1; }
    .project-card:hover {
        border-color: rgba(201,169,110,0.5);
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 20px 50px rgba(201,169,110,0.2);
    }
    .project-card:hover::after { transform: scaleX(1); }

    /* =============================
       EXPANDERS
       ============================= */
    .streamlit-expanderHeader {
        background: var(--navy-mid) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: var(--ivory) !important;
        font-family: 'DM Sans', sans-serif !important;
    }
    .streamlit-expanderContent {
        border: 1px solid var(--border) !important;
        border-top: none !important;
        background: rgba(13,27,42,0.5) !important;
    }

    </style>
    """


def section_header(label: str, title: str, divider: bool = True) -> str:
    """Returns HTML for a styled section header with optional divider."""
    html = f"""
    <p class="section-subheader">{label}</p>
    <h1 class="section-header">{title}</h1>
    """
    if divider:
        html += '<div class="divider"></div>'
    return html