import streamlit as st
import pandas as pd
import time

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Medicine Recommendation System",
    page_icon="💊",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* MAIN BACKGROUND */

[data-testid="stAppViewContainer"]{
    background:
    linear-gradient(
        135deg,
        #000000,
        #020617,
        #0f172a
    );
}

/* HEADER */

[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

/* SIDEBAR */

[data-testid="stSidebar"]{
    background: #020617;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* MAIN BLOCK */

.block-container{
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

/* TITLES */

h1{
    font-size: 64px !important;
    font-weight: 900 !important;

    background: linear-gradient(
        90deg,
        #38BDF8,
        #2563EB,
        #8B5CF6
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

h2,h3,h4,h5,h6{
    color: white !important;
}

/* TEXT */

p,label,div{
    color: #E2E8F0 !important;
}

/* HERO CARD */

.hero-card{
    background:
    linear-gradient(
        135deg,
        rgba(56,189,248,0.15),
        rgba(37,99,235,0.08),
        rgba(139,92,246,0.12)
    );

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 40px;

    backdrop-filter: blur(18px);

    margin-bottom: 30px;
}

/* METRIC CARDS */

[data-testid="metric-container"]{
    background:
    linear-gradient(
        135deg,
        rgba(255,255,255,0.06),
        rgba(255,255,255,0.03)
    );

    border: 1px solid rgba(255,255,255,0.08);

    padding: 20px;

    border-radius: 22px;

    backdrop-filter: blur(15px);

    transition: 0.3s;
}

[data-testid="metric-container"]:hover{
    transform: translateY(-4px);
    border: 1px solid #38BDF8;
}

/* INPUT */

.stTextInput > div > div > input{
    background: rgba(255,255,255,0.05);

    color: white !important;

    border-radius: 16px;

    border: 1px solid rgba(255,255,255,0.08);

    padding: 16px;

    font-size: 16px;
}

/* BUTTONS */

.stButton > button{
    width: 100%;

    background:
    linear-gradient(
        90deg,
        #0EA5E9,
        #2563EB,
        #8B5CF6
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 14px 24px;

    font-size: 16px;

    font-weight: 700;

    transition: 0.3s;
}

.stButton > button:hover{
    transform: scale(1.02);

    box-shadow: 0px 0px 25px rgba(56,189,248,0.5);
}

/* DATAFRAME */

[data-testid="stDataFrame"]{
    background: rgba(255,255,255,0.04);

    border-radius: 18px;

    padding: 12px;
}

/* TABS */

.stTabs [data-baseweb="tab-list"]{
    gap: 20px;
}

.stTabs [data-baseweb="tab"]{
    background: rgba(255,255,255,0.05);

    border-radius: 12px;

    padding: 10px 20px;

    color: white;
}

/* FOOTER */

.footer{
    text-align:center;

    padding:30px;

    margin-top:50px;

    border-top:1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(
    "data/small_medicine_dataset.csv",
    low_memory=False
)
    

    return df

df = load_data()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("💊 AI Dashboard")

st.sidebar.markdown("""
## 👨‍💻 Developer

### Sanat

📞 8629833620

📧 sarveshsharma6609@gmail.com

---

### 🚀 Technologies

- Python
- Streamlit
- Machine Learning
- Pandas
- Healthcare Analytics

---

### 📌 Features

✅ Medicine Search  
✅ Disease Search  
✅ Side Effects  
✅ Analytics Dashboard  
✅ AI Recommendation System  
""")

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero-card">

<h1>💊 AI Medicine Recommendation System</h1>

<h3>
Modern Healthcare Analytics Platform powered by Artificial Intelligence
</h3>

<p>
Analyze medicines, discover therapeutic insights,
search diseases, and explore healthcare analytics
through an advanced AI-powered dashboard.
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# METRICS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Records",
        f"{df.shape[0]:,}"
    )

with col2:
    st.metric(
        "Total Columns",
        df.shape[1]
    )

with col3:
    st.metric(
        "Therapeutic Classes",
        df['Therapeutic Class'].nunique()
    )

with col4:
    st.metric(
        "Habit Forming Types",
        df['Habit Forming'].nunique()
    )

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2, tab3 = st.tabs([
    "🔍 Medicine Search",
    "🩺 Disease Search",
    "📊 Analytics"
])

# --------------------------------------------------
# TAB 1
# --------------------------------------------------

with tab1:

    st.subheader("Search Medicines")

    medicine_name = st.text_input(
        "Enter Medicine Name"
    )

    search_btn = st.button(
        "Search Medicine"
    )

    if search_btn:

        with st.spinner(
            "Searching medicines..."
        ):

            time.sleep(1)

            result = df[
                df['name'].str.contains(
                    medicine_name,
                    case=False,
                    na=False
                )
            ]

            if not result.empty:

                st.success(
                    f"{len(result)} medicines found"
                )

                st.dataframe(
                    result[[
                        'name',
                        'use0',
                        'sideEffect0',
                        'Therapeutic Class',
                        'Habit Forming'
                    ]].head(20),
                    use_container_width=True
                )

            else:
                st.error(
                    "No medicine found"
                )

# --------------------------------------------------
# TAB 2
# --------------------------------------------------

with tab2:

    st.subheader(
        "Search by Disease / Use"
    )

    disease = st.text_input(
        "Enter Disease or Use"
    )

    disease_btn = st.button(
        "Search Disease"
    )

    if disease_btn:

        with st.spinner(
            "Finding medicines..."
        ):

            time.sleep(1)

            disease_result = df[
                df['use0'].str.contains(
                    disease,
                    case=False,
                    na=False
                )
            ]

            if not disease_result.empty:

                st.success(
                    f"{len(disease_result)} medicines found"
                )

                st.dataframe(
                    disease_result[[
                        'name',
                        'use0',
                        'sideEffect0',
                        'Therapeutic Class'
                    ]].head(20),
                    use_container_width=True
                )

            else:
                st.error(
                    "No matching results found"
                )

# --------------------------------------------------
# TAB 3
# --------------------------------------------------

with tab3:

    col5, col6 = st.columns(2)

    with col5:

        st.subheader(
            "📈 Top Therapeutic Classes"
        )

        top_classes = (
            df['Therapeutic Class']
            .value_counts()
            .head(10)
        )

        st.bar_chart(top_classes)

    with col6:

        st.subheader(
            "⚠ Habit Forming Analysis"
        )

        habit_counts = (
            df['Habit Forming']
            .value_counts()
        )

        st.bar_chart(habit_counts)

    st.subheader(
        "📋 Dataset Sample"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">

<h2>💊 AI Medicine Recommendation System</h2>

<p>Developed by <b>Sanat</b></p>

<p>📞 8629833620</p>

<p>📧 sarveshsharma6609@gmail.com</p>

<p>
Built using Python, Streamlit,
Machine Learning & Healthcare Analytics
</p>

</div>
""", unsafe_allow_html=True)
