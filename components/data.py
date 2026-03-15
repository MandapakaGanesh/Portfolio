"""
Portfolio data module.
All personal content, projects, skills, and experience data is defined here.
Edit this file to customize the portfolio with your own information.
"""

# ─── PERSONAL INFO ────────────────────────────────────────────────────────────
PERSONAL = {
    "name": "Mandapaka Ganesh",
    "name_first": "Mandapaka",
    "name_last": "Ganesh",
    "title": "Data Science & Analytics Student",
    "tagline": "Turning raw data into clear, actionable insights.",
    "intro": (
        "I'm a Computer Science Engineering student at Lovely Professional University "
        "with a strong passion for Data Science and Analytics. I enjoy working with "
        "real-world datasets — from cleaning and exploring to building dashboards and "
        "deriving actionable insights. Skilled in Python, Power BI, Excel, and MySQL, "
        "I'm eager to solve meaningful problems through data."
    ),
    "email": "ganeshmandapaka06@gmail.com",
    "linkedin": "https://linkedin.com/in/mandapaka-ganesh/",
    "github": "https://github.com/MandapakaGanesh",
    "location": "Phagwara, Punjab, IN",
    "status": "Open to Opportunities",
    "resume_file": "Mandapaka_Ganesh_Resume (1).pdf",
    "resume_image": "Mandapaka_Ganesh_Resume_page-0001.jpg",
}

# ─── EDUCATION ────────────────────────────────────────────────────────────────
EDUCATION = [
    {
        "year": "Aug 2023 – Present",
        "degree": "B.Tech — Computer Science & Engineering",
        "school": "Lovely Professional University, Phagwara, Punjab",
        "detail": "CGPA: 6.40",
        "icon": "🎓",
    },
    {
        "year": "Jun 2021 – May 2023",
        "degree": "Intermediate (Class XII)",
        "school": "Sri Viswa Junior College, Vizag, A.P.",
        "detail": "Percentage: 79%",
        "icon": "🏫",
    },
    {
        "year": "Jun 2020 – May 2021",
        "degree": "Matriculation (Class X)",
        "school": "Sri Chaitanya EM School, Vizag, A.P.",
        "detail": "Percentage: 97%",
        "icon": "🏆",
    },
]

# ─── CAREER INTERESTS ─────────────────────────────────────────────────────────
INTERESTS = [
    ("🔍", "Data Analytics",      "EDA, business intelligence & insight generation"),
    ("📊", "Data Visualization",  "Dashboards & storytelling with Power BI and Excel"),
    ("🗄️", "Database & SQL",      "Querying, managing, and analysing relational data"),
    ("🤖", "Machine Learning",    "Applying ML to real-world prediction problems"),
    ("🌐", "Web Technologies",    "Building clean interfaces with HTML & CSS"),
]

# ─── SKILLS ───────────────────────────────────────────────────────────────────
SKILLS = {
    "Programming": [
        ("Python",   85),
        ("C",        75),
        ("C++",      72),
        ("Java",     65),
        ("HTML/CSS", 70),
    ],
    "Data Analysis": [
        ("Pandas",            88),
        ("NumPy",             85),
        ("EDA",               87),
        ("Data Cleaning",     90),
        ("Statistical Analysis", 75),
    ],
    "Tools & Platforms": [
        ("Microsoft Excel",   90),
        ("Power BI",          82),
        ("MySQL",             80),
        ("Git / GitHub",      78),
        ("Jupyter Notebook",  85),
    ],
    "Visualization": [
        ("Matplotlib",        82),
        ("Seaborn",           80),
        ("Power BI Dashboards", 82),
        ("Excel Charts",      88),
        ("PivotTables",       85),
    ],
}

# ─── TOOLS ────────────────────────────────────────────────────────────────────
TOOLS = [
    ("🐍", "Python"),      ("🗄️", "MySQL"),       ("📊", "Power BI"),
    ("📗", "Excel"),       ("🐙", "Git/GitHub"),  ("📓", "Jupyter"),
    ("🐼", "Pandas"),      ("📐", "NumPy"),       ("📉", "Matplotlib"),
    ("🎨", "Seaborn"),     ("🌐", "HTML/CSS"),    ("☕", "Java"),
]

# ─── PROJECTS ─────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "title": "Salary Prediction",
        "category": "Machine Learning",
        "description": (
            "Employee Salary Prediction system using Linear Regression, Polynomial Regression, "
            "and Random Forest models to estimate compensation based on experience, education, "
            "and job role attributes. Architected a Scikit-learn preprocessing pipeline with "
            "StandardScaler, OneHotEncoder, and automated missing value imputation. Evaluated "
            "model performance using MAE, MSE, RMSE, and R² metrics with visualizations via "
            "scatter plots and comparative bar charts, with Random Forest achieving highest accuracy."
        ),
        "tech": ["Python", "Scikit-learn", "Linear Regression", "Random Forest", "Polynomial Regression"],
        "github": "https://github.com/MandapakaGanesh/Salary-Prediction-Project-Using-Machine-Learning",
        "demo": None,
        "highlights": [
            "Preprocessing pipeline with StandardScaler & OneHotEncoder",
            "Automated missing value imputation for clean inputs",
            "Random Forest achieved highest accuracy among tested models",
        ],
        "icon": "💰",
    },
    {
        "title": "Industrial Energy Insights Dashboard",
        "category": "Data Visualization",
        "description": (
            "A multi-page Power BI dashboard analyzing industrial energy consumption "
            "across load types (Light, Medium, Maximum), weekday/weekend patterns, "
            "and hourly usage. Tracks 417K+ kWh total energy, peak usage, CO2 "
            "emissions, and power factor metrics. Features a forecast chart, "
            "reactive power monitoring, load type distribution, and day-of-week "
            "usage trends with fully interactive slicers."
        ),
        "tech": ["Power BI", "DAX", "Data Modeling", "Forecasting"],
        "github": "https://github.com/MandapakaGanesh",
        "demo": None,
        "highlights": [
            "KPI cards: 417.31K kWh total energy, 151.31 kWh peak usage",
            "Forecast chart with confidence bands across load types",
            "Reactive power monitoring & load type distribution (donut chart)",
        ],
        "icon": "⚡",
    },
    {
        "title": "Abalone Data Analysis",
        "category": "Data Analysis",
        "description": (
            "Conducted a detailed exploratory analysis of the Abalone dataset to "
            "examine the relationship between shell measurements and age (Rings). "
            "Refined raw data using Pandas and NumPy, produced statistical "
            "summaries and correlation matrices, and created visualizations "
            "including pair plots, heatmaps, and box plots using Seaborn and "
            "Matplotlib to support predictive age modelling."
        ),
        "tech": ["Python", "Pandas", "NumPy", "Seaborn", "Matplotlib"],
        "github": "https://github.com/MandapakaGanesh",
        "demo": None,
        "highlights": [
            "Correlation matrix revealing key biological growth indicators",
            "Pair plots & heatmaps for pattern detection",
            "Insights supporting predictive age estimation models",
        ],
        "icon": "🐚",
    },
    {
        "title": "Avocado Ripeness Analysis (Training Capstone)",
        "category": "Machine Learning",
        "description": (
            "Comprehensive analysis of avocado ripeness using historical market "
            "and quality datasets as the capstone of a summer training program. "
            "Cleaned and structured raw data in Excel, performed EDA in Python, "
            "and designed interactive Power BI dashboards to visualize ripeness "
            "patterns across regions and time periods, delivering supply chain "
            "insights to reduce food waste."
        ),
        "tech": ["Python", "Pandas", "NumPy", "Power BI", "Excel", "Machine Learning"],
        "github": "https://github.com/MandapakaGanesh",
        "demo": None,
        "highlights": [
            "Interactive Power BI dashboard by region & time period",
            "EDA identifying ripeness and size characteristic trends",
            "Actionable insights to optimize avocado distribution",
        ],
        "icon": "🥑",
    },
    {
        "title": "Retail Store Analysis",
        "category": "Data Analysis",
        "description": (
            "Comprehensive retail store performance analysis examining sales patterns, "
            "customer behavior, and inventory metrics. Conducted exploratory data analysis "
            "to identify key business drivers, seasonal trends, and product performance. "
            "Developed actionable recommendations for optimizing stock levels, improving "
            "customer satisfaction, and increasing revenue through data-driven decision making."
        ),
        "tech": ["Python", "Pandas", "NumPy", "Seaborn", "Matplotlib", "Excel"],
        "github": "https://github.com/MandapakaGanesh/Retail-Stoer-Analysis",
        "demo": None,
        "highlights": [
            "Sales trend analysis revealing seasonal patterns and peak periods",
            "Customer segmentation and purchasing behavior insights",
            "Inventory optimization recommendations based on demand forecasting",
        ],
        "icon": "🏪",
    },
]

CATEGORIES = ["All"] + sorted(list(set(p["category"] for p in PROJECTS)))

# ─── CERTIFICATES ─────────────────────────────────────────────────────────────
CERTIFICATES = [
    {
        "title": "Cloud Computing",
        "issuer": "NPTEL",
        "date": "Oct 2025",
        "icon": "☁️",
    },
    {
        "title": "Solutions Architecture Job Simulation",
        "issuer": "Forage",
        "date": "Sep 2025",
        "icon": "☁️",
    },
    {
        "title": "Responsive Web Design",
        "issuer": "freeCodeCamp",
        "date": "Oct 2023",
        "icon": "🌐",
    },
    {
        "title": "Data Visualization: Business Analytics Job Simulation",
        "issuer": "Tata Group",
        "date": "Oct 2023",
        "icon": "📊",
    },
]

# ─── CERTIFICATE LINKS (Optional) ─────────────────────────────────────────────
CERTIFICATE_LINKS = {
    "Solutions Architecture Job Simulation": "https://drive.google.com/file/d/131QvPjgDnWc6IUiMKAv3RAqu7ObVB3W8/view",
    "Data Visualization: Business Analytics Job Simulation": "https://www.theforage.com/completion-certificates/ifobHAoMjQs9s6bKS/MyXvBcppsW2FkNYCX_ifobHAoMjQs9s6bKS_QaLhef2oPJm88iTbb_1758175749632_completion_certificate.pdf",
    "Responsive Web Design": "https://www.freecodecamp.org/certification/ganeshmandapaka/responsive-web-design",
    "Cloud Computing": "https://drive.google.com/file/d/1_Q9iOe37o9sdkLMXm2AZfogxvvSPuZJV/view",
}

# ─── ACHIEVEMENTS ─────────────────────────────────────────────────────────────
ACHIEVEMENTS = [
    {
        "title": "Webka Hackathon — Final Round",
        "date": "Jan 2024",
        "detail": "Selected for the final round for demonstrating innovative project design and strong technical implementation.",
        "icon": "🏅",
    },
    {
        "title": "LPU Data Science Summer Training",
        "date": "Jun–Jul 2025",
        "detail": "Completed hands-on training in MySQL, Excel, Power BI, and Machine Learning with a capstone project on avocado ripeness analysis.",
        "icon": "🎓",
    },
]

# ─── STATS ────────────────────────────────────────────────────────────────────
STATS = [
    ("3+",  "Projects Completed"),
    ("6.40", "CGPA"),
    ("4+",  "Certificates"),
    ("97%", "Class X Score"),
]