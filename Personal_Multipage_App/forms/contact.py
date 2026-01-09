import streamlit as st

def contact_form():
    with st.form("contact_form"):
        st.header("Contact Me")
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success("Message successfully sent!")