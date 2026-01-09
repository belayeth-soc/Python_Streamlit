import streamlit as st
import pandas as pd


st.title("Customer Satisfaction Survey")
st.write("We value your feedback! Please take a moment to answer these 10 questions.")


# Use st.form to ensure all questions are submitted together
with st.form("survey_form"):
    # 1. Open-ended (Identifier)
    cust_id = st.text_input("Your Name or Customer ID")
    # 2. Closed-ended: Slider (1-10)
    sat_score = st.slider("1. How satisfied are you with our service? (1=Low, 10=High)", 1, 10, 5)

    # 3-7. Closed-ended: Multiple Choice (Radio/Selectbox)
    ease = st.radio("2. How easy is it to use our platform?", ["Very Easy", "Somewhat Easy", "Neutral", "Difficult"])
    quality = st.selectbox("3. How would you rate the quality of our service?", ["Excellent", "Good", "Average", "Poor"])
    variety = st.radio("4. Are you satisfied with our product variety?", ["Yes", "Mostly", "Neutral", "No"])
    pricing = st.radio("5. How do you feel about our pricing?", ["Great Value", "Fair", "Expensive"])
    speed = st.selectbox("6. Rate our response speed:", ["Instant", "Fast", "Acceptable", "Slow"])

    # 8. Closed-ended: Likelihood (1-10)
    recommend = st.slider("7. How likely are you to recommend us to a friend?", 1, 10, 8)

    # 9. Closed-ended: Category selection
    support = st.radio("8. Rate your recent support experience:", ["N/A", "Very Helpful", "Helpful", "Unhelpful"])

    # 10-11. Open-ended: Qualitative feedback
    improvements = st.text_area("9. What is one thing we could do to improve your experience?")
    comments = st.text_area("10. Any other additional comments?")

    # Submit button for the form
    submitted = st.form_submit_button("Submit Survey")

if submitted:
    if not cust_id:
        st.error("Please provide your Name or Customer ID before submitting.")
    else:
        # Create a dictionary of results
        survey_data = {
            "CUSTOMER_ID": [cust_id],
            "OVERALL_SATISFACTION": [sat_score],
            "EASE_OF_USE": [ease],
            "SERVICE_QUALITY": [quality],
            "PRODUCT_VARIETY": [variety],
            "PRICING_SATISFACTION": [pricing],
            "SPEED_OF_SERVICE": [speed],
            "RECOMMEND_LIKELIHOOD": [recommend],
            "SUPPORT_EXPERIENCE": [support],
            "IMPROVEMENT_SUGGESTIONS": [improvements],
            "ADDITIONAL_COMMENTS": [comments]
        }
        
        # Convert to DataFrame and write to Snowflake
        df = pd.DataFrame(survey_data)
        try:
            session.write_pandas(df, "CUSTOMER_SURVEY_RESULTS", overwrite=False)
            st.success("Thank you! Your feedback has been recorded.")
            st.balloons()
        except Exception as e:
            st.error(f"Failed to save data: {e}")