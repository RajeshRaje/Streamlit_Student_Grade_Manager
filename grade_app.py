"""
Premium Student Grade Manager — Week 1, Day 4
Run: streamlit run grade_app.py
Install: python -m pip install streamlit
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GradeFlow | Student Manager",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Premium visual styling ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@500;600;700;800&display=swap');

    :root {
        --ink: #17233b;
        --muted: #718096;
        --line: #e8edf5;
        --blue: #4568f5;
        --violet: #7957e8;
        --surface: #ffffff;
        --bg: #f5f7fc;
    }
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }
    .stApp {
        background:
            radial-gradient(900px 420px at 5% -10%, rgba(95,119,255,.11), transparent 65%),
            radial-gradient(700px 380px at 100% 0%, rgba(139,92,246,.09), transparent 60%),
            var(--bg);
        color: var(--ink);
    }
    .block-container {
        max-width: 1240px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .brand-row {
        display:flex; align-items:center; justify-content:space-between;
        margin-bottom: 1.25rem;
    }
    .brand {
        display:flex; align-items:center; gap:11px;
        color:#17233b; font-weight:800; letter-spacing:-.4px;
        font-family:'Manrope',sans-serif; font-size:1.05rem;
    }
    .brand-mark {
        width:38px; height:38px; border-radius:12px;
        display:flex; align-items:center; justify-content:center;
        color:white; font-size:19px;
        background:linear-gradient(135deg,#4568f5,#8057e9);
        box-shadow:0 7px 18px rgba(69,104,245,.25);
    }
    .top-pill {
        border:1px solid #e3e9f5; background:rgba(255,255,255,.8);
        color:#65738a; padding:8px 13px; border-radius:999px;
        font-size:12px; font-weight:700;
    }
    .hero {
        position:relative; overflow:hidden; border-radius:24px;
        padding:30px 34px; color:white;
        background:linear-gradient(115deg,#172b55 0%,#304b9d 55%,#6a55cb 100%);
        box-shadow:0 18px 45px rgba(35,55,112,.18);
        margin-bottom:25px;
    }
    .hero:after {
        content:""; position:absolute; width:290px; height:290px;
        border:1px solid rgba(255,255,255,.13); border-radius:50%;
        right:8%; top:-155px; box-shadow:0 0 0 35px rgba(255,255,255,.035),
        0 0 0 70px rgba(255,255,255,.025);
    }
    .eyebrow {
        text-transform:uppercase; letter-spacing:1.8px;
        font-size:10px; font-weight:800; color:#c9d5ff; margin-bottom:10px;
    }
    .hero h1 {
        font-family:'Manrope',sans-serif; font-size:clamp(28px,4vw,39px);
        line-height:1.12; letter-spacing:-1.3px; color:white;
        margin:0 0 9px 0; font-weight:800;
    }
    .hero p {color:#dce5ff; font-size:14px; margin:0; max-width:580px;}
    .hero-tag {
        display:inline-block; margin-top:19px; padding:7px 11px;
        border:1px solid rgba(255,255,255,.23); border-radius:9px;
        color:#f1f4ff; font-size:11px; font-weight:700;
        background:rgba(255,255,255,.08);
    }
    .section-head {
        display:flex; align-items:end; justify-content:space-between;
        margin:24px 0 13px 0;
    }
    .section-title {
        color:#192744; font-family:'Manrope',sans-serif;
        font-weight:800; font-size:18px; letter-spacing:-.4px;
    }
    .section-sub {color:#8490a5; font-size:12px; margin-top:3px;}
    div[data-testid="stForm"] {
        background:rgba(255,255,255,.94); border:1px solid var(--line);
        border-radius:18px; padding:20px 22px 12px 22px;
        box-shadow:0 8px 24px rgba(31,48,86,.045);
    }
    div[data-testid="stTextInput"] label, div[data-testid="stNumberInput"] label {
        color:#53627b; font-size:12px; font-weight:700;
    }
    div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {
        border-radius:10px; border-color:#e1e7f0; background:#fbfcff;
    }
    div[data-testid="stTextInput"] input:focus, div[data-testid="stNumberInput"] input:focus {
        border-color:#7188ff; box-shadow:0 0 0 2px rgba(69,104,245,.10);
    }
    div.stButton > button, div[data-testid="stFormSubmitButton"] button {
        border:0; border-radius:10px; min-height:43px; font-weight:800;
        color:white; background:linear-gradient(100deg,#4568f5,#7658e8);
        box-shadow:0 7px 16px rgba(69,104,245,.20);
        transition:transform .15s ease, box-shadow .15s ease;
    }
    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover {
        color:white; transform:translateY(-1px);
        box-shadow:0 10px 20px rgba(69,104,245,.27);
    }
    div[data-testid="stMetric"] {
        background:white; border:1px solid var(--line); border-radius:17px;
        padding:17px 19px; box-shadow:0 8px 24px rgba(31,48,86,.045);
    }
    div[data-testid="stMetricLabel"] {
        color:#7a879d; font-size:11px; font-weight:800;
        text-transform:uppercase; letter-spacing:.7px;
    }
    div[data-testid="stMetricValue"] {
        color:#1c2b49; font-family:'Manrope',sans-serif;
        font-size:29px; font-weight:800;
    }
    div[data-testid="stDataFrame"] {
        border:1px solid var(--line); border-radius:15px; overflow:hidden;
        background:white;
    }
    .empty-state {
        padding:32px 20px; border:1px dashed #d8e0ed;
        border-radius:17px; background:rgba(255,255,255,.72);
        text-align:center; color:#8490a5;
    }
    .empty-icon {font-size:28px; margin-bottom:8px;}
    .empty-title {color:#34425d; font-weight:800; font-size:14px;}
    .empty-copy {font-size:12px; margin-top:4px;}
    .footer {
        border-top:1px solid #e6ebf3; margin-top:35px; padding-top:16px;
        display:flex; justify-content:space-between; color:#9aa5b7;
        font-size:11px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Grading logic: identical to Day 2 ----------
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    return "E"


# ---------- Persistent session data ----------
if "students" not in st.session_state:
    st.session_state.students = []

# ---------- Header ----------
st.markdown(
    """
    <div class="brand-row">
      <div class="brand"><div class="brand-mark">G</div> GradeFlow</div>
      <div class="top-pill">WEEK 1&nbsp; / &nbsp;DAY 4&nbsp; · &nbsp;STUDENT ANALYTICS</div>
    </div>
    <div class="hero">
      <div class="eyebrow">Academic performance dashboard</div>
      <h1>Student Grade Manager</h1>
      <p>A clearer view of every student's progress. Add marks, track grades, and understand your class performance at a glance.</p>
      <span class="hero-tag">✦ &nbsp; Simple. Smart. Organized.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Add student form ----------
st.markdown(
    """
    <div class="section-head">
      <div><div class="section-title">Add a student</div>
      <div class="section-sub">Enter the student's details below to update your class register.</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("add_student_form", clear_on_submit=True):
    col_name, col_mark, col_submit = st.columns([2.1, 1.2, 0.9], vertical_alignment="bottom")
    with col_name:
        name = st.text_input("STUDENT NAME", placeholder="e.g. Priya Sharma")
    with col_mark:
        mark = st.number_input(
            "MARK (0–100)", min_value=0.0, max_value=100.0,
            value=0.0, step=1.0, format="%.1f"
        )
    with col_submit:
        submitted = st.form_submit_button("＋  Add student", use_container_width=True)

if submitted:
    cleaned_name = name.strip()
    if not cleaned_name:
        st.error("Please enter a student name.")
    elif not 0 <= mark <= 100:
        st.error("Mark must be between 0 and 100.")
    else:
        st.session_state.students.append(
            {"Name": cleaned_name, "Mark": float(mark), "Grade": get_grade(float(mark))}
        )
        st.success(f"{cleaned_name} has been added to the class register.")

# ---------- Dashboard ----------
students = st.session_state.students
st.markdown(
    """
    <div class="section-head">
      <div><div class="section-title">Class overview</div>
      <div class="section-sub">Live performance summary for your students.</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

if students:
    marks = [student["Mark"] for student in students]
    average = sum(marks) / len(marks)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total students", len(students), help="Number of students in the register")
    m2.metric("Class average", f"{average:.1f} / 100")
    m3.metric("Highest mark", f"{max(marks):g}")
    m4.metric("Lowest mark", f"{min(marks):g}")

    st.markdown(
        """
        <div class="section-head">
          <div><div class="section-title">Student register</div>
          <div class="section-sub">All submitted student marks and assigned grades.</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    df = pd.DataFrame(students)
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Name": st.column_config.TextColumn("Student name", width="large"),
            "Mark": st.column_config.NumberColumn("Mark", format="%.1f / 100"),
            "Grade": st.column_config.TextColumn("Grade", width="small"),
        },
    )

    grade_counts = df["Grade"].value_counts()
    grade_order = ["A", "B", "C", "D", "E"]
    grade_summary = {grade: int(grade_counts.get(grade, 0)) for grade in grade_order}
    with st.expander("View grade distribution"):
        dist_cols = st.columns(5)
        for col, grade in zip(dist_cols, grade_order):
            col.metric(f"Grade {grade}", grade_summary[grade])
else:
    st.markdown(
        """
        <div class="empty-state">
          <div class="empty-icon">📚</div>
          <div class="empty-title">Your class register is ready</div>
          <div class="empty-copy">Add your first student using the form above. Your class metrics and results will appear here.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="footer">
      <span>GRADEFlow &nbsp;·&nbsp; STUDENT GRADE MANAGER</span>
      <span>Built with Streamlit &nbsp;✦&nbsp; Data stays in this session</span>
    </div>
    """,
    unsafe_allow_html=True,
)
