from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "A.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Abhiraj Sachan"
PAGE_ICON = ":wave:"
NAME = "Abhiraj sachan"
DESCRIPTION = """
 a passionate machine learning student and having a knowledge in dsa , python oops and in sql.
"""
EMAIL = "abhirajsachan706@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/abhiraj-sachan-542799222/",
    "GitHub": "https://github.com/abhiraj-sac",
    "Twitter": "https://twitter.com/rajabhi1334607",
    "My Blogs at medium": "https://medium.com/@abhirajj701",
    "Kaggle": "https://www.kaggle.com/abhirajsac",
    "Leetcode": "https://leetcode.com/abhirajsac/",
    "GFG": "https://auth.geeksforgeeks.org/user/abhirajsachan706",
}
PROJECTS = {
    "🏆 Top sql questions - Blog on top sql questions ": "https://medium.com/@abhirajj701/top-8-sql-queries-sql-interview-questions-for-data-science-e791dff3ba4d",
    "🏆 From the vault - Python oops concepts on medium": "https://medium.com/@abhirajj701/python-oops-concept-c1abc5778b18",
    "🏆 Appling linear regression without using sklearn libraries.": "https://medium.com/@abhirajj701/implementing-simple-linear-regression-without-using-scikit-learn-classes-8cecd4b246d2",
    "🏆 About simple linear regression": "https://medium.com/@abhirajj701/what-is-simple-linear-regression-67a3d2df970b",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

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


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qulifications & Qualities")
st.write(
    """
- ✔️ Schooling from Lucknow public college
  ✔️ Bca from Galgotias university
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA , Java
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MySQL
- In the past i have done android developement.
- Statistical programming
- Probability and statistics
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("My projects")
st.write("---")

# --- JOB 1

    
# st.markdown("[visit Github][https://github.com/abhiraj-sac/Spam_detector-End-to-End-deployed-project]")
pro ={
    "SMS spam trapper project ---> Github Link":"https://github.com/abhiraj-sac/Spam_detector-End-to-End-deployed-project",
    " Car price ---> Github Link": "https://github.com/abhiraj-sac/Car_price_prediction",
    "Flipcart web scrapping ---> Github Link":"https://github.com/abhiraj-sac/WEB-SCRAPPING-FLIPCART"


}
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(pro.items()):
    cols[index].write(f"[{platform}]({link})")
st.write("""The sms spam trapper is a end to end machine learning project, which is deployed in Render.All steps are included in this projects which are:-
            Collecting Data: As you know, machines initially learn from the data that you give them. ...
            Preparing the Data: After you have your data, you have to prepare it. ...
            Choosing a Model: ...
            Training the Model: ...
            Evaluating the Model: ...
            Parameter Tuning: ...
            Making Predictions.
            I have vs code for making a python application.The sms spam trapper is a end to end machine learning project, which is deployed in Render.All steps are included in this projects which are:- Collecting Data: As you know, machines initially learn from the data that you give them. ... Preparing the Data: After you have your data, you have to prepare it. ... Choosing a Model: ... Training the Model: ... Evaluating the Model: ... Parameter Tuning: ... Making Predictions. I have vs code for making a python application.
            Skills: Pickles · Heroku · Random Forest · Scikit-Learn · Git · Matplotlib · NumPy · Pandas (Software)""")
st.subheader("Car price predictor project summary")
st.write("""
            The main aim of this project is to predict the price of used cars using various Machine Learning (ML) models.
            Steps Involved
            Data Cleaning which involves identifying all the null and missing values and removing the outliers
            The next process is Data Preprocessing which involves us normalising and standardize the dataset
            We then use the different Machine Learning models like Linear Regression, KNN
            We then need to compare the performance of any of the models used
            Now, gather insights and analyze the data based on the accuracy test""")


# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("My blogs")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
