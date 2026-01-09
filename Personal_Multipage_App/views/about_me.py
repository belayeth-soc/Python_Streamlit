import streamlit as st
from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
        contact_form()

# ----- HERO SECTION -----
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/headshot.png", width=180, caption=None)
with col2:
        st.title("Belayeth Hussain", anchor=False)
        st.write(
            "Social Science Researcher; Data Science Enthusiast; Impact Evaluation Specialist"
            )

        if st.button("Contact Me"):
            show_contact_form()
            
            
# ----- EXPERIENCE -----
st.write("\n")
st.subheader("Experience", anchor=False)
st.write("""
                - Senior Researcher, Data Science Expert Team, JBS International, USA
                - Research Associate-II, JBS International, USA
                - Consultant, CareerFoundry, Germany
                - Senior Lecturer, University of Science, Malaysia
                - Professor-Lecturer, Shahjalal University of Science & Technology, Bangladesh
                - Postdoctoral Researcher, University of Science, Malaysia
                """)

 # ---- EDUCATION -----
st.write("\n")
st.subheader("Education", anchor=False)
st.write("""
                - Ph.D. in Social Science, University of Kassel, Germany
                - M.A. in Development Studies, University of Antwerp, Belgium
                - M.S.S. in Sociology, Shahjalal University of Science & Technology, Bangladesh
                - B.S.S. in Sociology, Shahjalal University of Science & Technology, Bangladesh
                """)
 
# ----- SKILLS -----
st.write("\n")
st.subheader("Skills", anchor=False)
st.write("""
                - Social Data Science
                - Program Evaluation
                - Mixed Methods Research
                - Statistical Analysis (R, Python, SPSS, SAS)
                - Data Visualization (Tableau, Power BI, Streamlit)
                - Machine Learning
                """)

# ----- DOMAIN EXPERTISE -----
st.write("\n")
st.subheader("Domain Expertise", anchor=False)
st.write("""
                - Labor Standards & Workforce Development
                - Public Health
                - Child Welfare
                - Social Capital & Community Development
                - Sustainable Development
                - Climate Change
                """)
          