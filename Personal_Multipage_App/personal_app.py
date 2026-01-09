import streamlit as st
#from PIL import Image

#logo = Image.open("Personal_Multipage_App/assets/sg_logo.jpg")
#headshot = Image("Personal_Multipage_App/assets/sg_headshot.png")


# ----- PAGE SETUP 
st.set_page_config(layout="wide")
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="👨‍💻",
    default=True,
)

project_page = st.Page(
    page="views/projects.py",
    title="Select Projects",
    icon="📁",
)
skill_page = st.Page(
    page="views/skills.py",
    title="Skills & Expertise",
    icon="💻",
)
publication_page = st.Page(
    page="views/publications.py",
    title="Publications",
    icon="📄",
)
blog_page = st.Page(
    page="views/blog.py",
    title="Blog Posts",
    icon="📝",
)   

# ----- NAVIGATION SETUP (WITHOUT SECTIONS) 

pg = st.navigation(
    pages=[
        about_page,
        project_page,
        skill_page,
        publication_page,
        blog_page,
    ],
)

# ----- NAVIGATION SETUP (WITH SECTIONS) USING DICTIONARY -----


# ----- SHARED ON ALL PAGES -----
#st.logo("assets/sg_logo.jpg", size="large")
st.sidebar.text("Created with Streamlit ❤️ by Belayeth")


# ----- RUN NAGIVATION -----
pg.run()

