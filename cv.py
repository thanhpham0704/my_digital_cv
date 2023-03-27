
from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "thanh.jpeg"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Tan Thanh Pham"
PAGE_ICON = ":wave:"
layout = 'wide'
NAME = "Tan Thanh Pham"
DESCRIPTION = """
Junior Data Analyst, experienced in education sector with a demonstrated history of working in the education management industry. Skilled in Tableau, SQL, Excel and Python. Strong academic background and English proficiency with a First Class Honours Bachelor degree in Business Management from University of Sunderland and IELTS 8.0 certificate.
"""
EMAIL = "thanhpham074@gmail.com"
PHONE = "0327970915"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/thanh-pham-0baa911aa/",
    "GitHub": "https://github.com/thanhpham0704",
    "Facebook": "https://www.facebook.com/phamtanthanh074"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=layout)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📞", PHONE)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✅ 1 year experience extracting actionable insights from data
- ✅ 3-year-experience IELTS teacher communicating and presenting in an easy-to-understand manner
- ✅ Strong hands-on experience and knowledge in Python, SQL, Tableau and Excel
- ✅ Good understanding of statistical principles and their respective applications
- ✅ Excellent self-learner with high sense of responsibility
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👨‍💻 Programming: Python (pandas, numpy, scipy, matplotlib, seaborn, plotly)
- 📊 Data Visulization: Tableau, MS Excel
- 🕸 Web Development: Streamlit
- ⚙️ Automation: Python (gspread, sqlalchemy)
- 📚 Modeling: Linear regression
- 🗄️ Database: MySQL, Oracle, Microsoft SQL Server, PostgreSQL, phpMyAdmin

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | IELTS Vietop**")
st.write("03/2022 - Present")
st.write(
    """
- ► Created, hosted and managed a Learning Management System for online replacement and periodic tests that results in 100% workload reduction
- ► Used Python to get data from API and then Tableau to create dashboards that boost operating process by 50%, and get new insights on teachers and sellers performance
- ► Used Python and Tableau to perform ad-hoc analysis for Operation, Education, Finance, Sale, HR and Marketing department to assist decision-making
- ► Used Python's Streamlit framework to automate and host salary calculation web app for Finance Department
- ► Led 1 more analyst to build a database for HR department

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**IELTS teacher | IELTS Vietop**")
st.write("09/2020 - 04/2023")
st.write(
    """
- ► Used PowerPoint, Kahoot, Quizlet to create and present ideas in a clear and engaging manner for a group of 8 to 10 students
- ► Taught students how to describe different kinds of graphs, charts, maps and process in written language

""")
PROJECTS = {
    "🏆 Operation Dashboard - Describing students and classes that need to be take care of": "https://public.tableau.com/views/Baoluu/DashboardCM?:language=en-US&:display_count=n&:origin=viz_share_link",
    "🏆 Regression module - Building a regression model to predict the number of time taken to achieve a specific score": "https://thanhpham0704-score-time-regressio-score-time-regression-7hh1pi.streamlit.app/",
    "🏆 Placement Test Conversion Rate Dashboard - Comparing conversion rate across teachers who conducted replacement test": "https://public.tableau.com/views/DashboardTlchuynitestuvo/Conversion_rate?:language=en-US&:display_count=n&:origin=viz_share_link",
    "🏆 Academic Dashboard - Keeping track of students' learning path and teachers' performance": "https://public.tableau.com/views/DashboardQLT_16686521824130/DashboardQLT?:language=en-US&:display_count=n&:origin=viz_share_link",
    "🏆 Sale Dashboard - Comparing sales, KPI, revenue across sellers and months to help set up KPI ": "https://public.tableau.com/views/DashboardEC_16693426224880/Story1?:language=en-US&:display_count=n&:origin=viz_share_link",
    "🏆 Time Attendance Dashboard - Transforming data from attendance device to create HR's report": "https://public.tableau.com/views/Bocochmcng/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link",
    "🏆 Accounting app - Automating financial report and salary calculation for finance department": "https://vietoptaichinh.streamlit.app/",
    "🏆 Marketing Dashboard - Describing various metrics for better marketing targeting": "https://public.tableau.com/views/DashboardMarketing_16696955897620/Story2?:language=en-US&:display_count=n&:origin=viz_share_link",
}

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
