import streamlit as st

st.title("📋 Snowflake Survey Form")

likert_options = ["Strongly agree", "Agree", "Neutral", "Disagree", "Strongly disagree"]

# 1-4: Likert Questions
q1 = st.radio("1. The interface is easy to navigate.", options=likert_options)
q2 = st.radio("2. The data processing speed is satisfactory.", options=likert_options)
q3 = st.radio("3. The documentation provided is clear.", options=likert_options)
q4 = st.radio("4. Overall, I am satisfied with the service.", options=likert_options)

st.divider()

# 5: The Trigger Question (Moved out of form for instant reaction)
q5 = st.selectbox("5. Did you encounter any technical issues today?", options=["No", "Yes"])

# 6: The Conditional Question
q6 = ""
if q5 == "Yes":
    q6 = st.text_area("6. Please describe the issues you encountered:")

# 7-9: Open Ended
q7 = st.text_area("7. What features do you use most frequently?")
q8 = st.text_area("8. What is one thing we could improve?")
q9 = st.text_area("9. Any additional comments or suggestions?")

# Submit Button (Since we aren't using st.form, we use a standard button)
if st.button("Submit Survey"):
    # Logic to save to Snowflake goes here
    st.success("Thank you! Your responses have been recorded.")