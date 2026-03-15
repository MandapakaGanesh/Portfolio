# 📊 Data Science Portfolio — Mandapaka Ganesh

A professional, elegant personal portfolio built with **Python + Streamlit**.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install streamlit

# 2. Run the app
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

---

## 📁 Project Structure

```
portfolio/
├── app.py                   # Main entry point & router
├── requirements.txt
├── components/
│   ├── __init__.py
│   ├── data.py              # ← Edit YOUR info here
│   ├── styles.py            # Global CSS & helpers
│   └── sidebar.py           # Sidebar navigation
├── pages/
│   ├── __init__.py
│   ├── home.py              # Hero / landing page
│   ├── about.py             # Education, tools, interests
│   ├── projects.py          # Project cards + filter
│   ├── skills.py            # Skills dashboard
│   ├── resume.py            # Resume preview + download
│   └── contact.py           # Contact form + social links
└── assets/
    └── (place resume PDF here as Mandapaka_Ganesh_Resume.pdf)
```

---

## ✏️ Customizing

All personal content is in **`components/data.py`**. Edit:

| Variable    | What it controls                     |
|-------------|--------------------------------------|
| `PERSONAL`  | Name, title, bio, email, links       |
| `EDUCATION` | Degrees and certifications           |
| `INTERESTS` | Career interest cards                |
| `SKILLS`    | Skill categories + proficiency %     |
| `TOOLS`     | Tools & tech badges                  |
| `PROJECTS`  | Project cards with links             |
| `STATS`     | Headline stats on home page          |

### Adding Your Resume PDF

Place your resume at `assets/resume.pdf` and update `resume.py`:
```python
# In pages/resume.py, replace _generate_resume_placeholder() with:
with open("assets/resume.pdf", "rb") as f:
    data = f.read()
```

### Adding a Profile Photo

Replace the emoji avatar in `pages/home.py` with:
```python
from PIL import Image
img = Image.open("assets/profile.jpg")
st.image(img, width=200)
```

---

## 🎨 Design System

| Token          | Value     | Used for              |
|----------------|-----------|-----------------------|
| `--navy`       | `#0D1B2A` | Main background       |
| `--navy-mid`   | `#1B2B3B` | Cards, sidebar        |
| `--gold`       | `#C9A96E` | Accents, highlights   |
| `--mist`       | `#B8CDD9` | Body text             |
| `--steel`      | `#7A93AC` | Secondary text        |
| `--success`    | `#4CAF82` | Status indicators     |

Fonts: **Cormorant Garamond** (headings) · **DM Sans** (body) · **DM Mono** (code)

---

## 🌐 Deploy to Streamlit Cloud

1. Push to a GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo → set `app.py` as entry point
4. Deploy!
