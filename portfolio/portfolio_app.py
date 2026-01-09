import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
from PIL import Image

# Set page configuration
st.set_page_config(layout="wide")

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
# Load Lottie animation files               
lottie_program = load_lottie_file("json/program.json")
project_image = Image.open("/Users/belayeth/Documents/Python programming/Python_Streamlit/portfolio/project.png")

#st.title("Professional Portfolio")
#st_lottie(lottie_program, 
          #speed=1,
          #reverse=False,
          #loop=True,
          #quality="high", # medium ; high
          #renderer="svg", # canvas ; svg
          #height=200,
          #width=200,
          #key=None,
          #)

with st.container():
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.header("Belayeth Hussain, Ph.D.")
#st.subheader("Social Data Science | Program Evaluation | Mixed Methods Research")
#st.write("[Read More on LinkedIn](https://www.linkedin.com/in/belayeth)")
#Add containers for different menu sections (icons imported from bootstrap icons)
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Skills", "Publications", "Blogs", "Contact"],
        icons=["house", "folder", "code-slash", "file-earmark-text", "journal-text", "envelope"],
        orientation="horizontal",
        styles= "Any",
        default_index=0,
    )

    if selected == "Home":
        with st.container():
            col1, col2, col3= st.columns([1,1,1])
            
            with col2: #add a Lottie animation here
                st_lottie(lottie_program, 
                          speed=2,
                          reverse=False,
                          loop=True,
                          quality="high", # medium ; high
                          #renderer="svg", # canvas ; svg
                          height=200,
                          width=200,
                          key=None,
                        )
                st.write("##")
            
            
            with col1:
                #st.title("About Me")
                st.subheader("About Me")
                st.markdown("""Senior Researcher with over 20 years of experience in multidisciplinary research settings, project management, mentoring, and stakeholder relations. 
                            Expertise includes social policies, program evaluations, and public health, with a focus on predictive data science, analytics modeling, performance evaluation, 
                            and dynamic data storytelling through data dashboards. Authored over 30 scholarly papers, books, and chapters, advancing social science research. Passionate about 
                            using mixed-method to enhance programs and policies in collaborative environments that yield tangible societal impact.""")


        with st.container():
            col3, col4, col5 = st.columns(3)
            with col3: #Define education and experience here
                st.subheader("Education")
                st.write("""
                - Ph.D. in Social Science, University of Kassel, Germany
                - M.A. in Development Studies, University of Antwerp, Belgium
                - M.S.S. in Sociology, Shahjalal University of Science & Technology, Bangladesh
                - B.S.S. in Sociology, Shahjalal University of Science & Technology, Bangladesh
                """)
            with col4: #Define skills and expertise here
                st.subheader("Experience")
                st.write("""
                - Senior Researcher, Data Science Expert Team, JBS International, USA
                - Research Associate-II, JBS International, USA
                - Consultant, CareerFoundry, Germany
                - Senior Lecturerer, University of Science, Malaysia
                - Professor-Lecturerer, Shahjalal University of Science & Technology, Bangladesh
                - Postdoctoral Researcher, University of Science, Malaysia
                """)
            with col5: #Define skills and expertise here
                st.subheader("Skills & Expertise")
                st.write("""
                - Social Data Science
                - Program Evaluation
                - Mixed Methods Research
                - Statistical Analysis (R, Python, SPSS, Stata)
                - Data Visualization
                - Machine Learning
                """)
        #st.subheader("Welcome to My Professional Portfolio")
        #st.write("Explore my projects, skills, publications, and more.")
        
    if selected == "Projects":
        with st.container():
            st.subheader("My Projects")
            st.write("List of select projects accomplished and currently working on")
            
            col6, col7 = st.columns([1,2])
            with col6:
                st.image(project_image)
            with col7:
                st.write("Description of Project 1")
                st.write("Description of Project 2")
                st.write("Description of Project 3")