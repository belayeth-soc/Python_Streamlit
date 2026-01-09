import streamlit as st
#from snowflake.snowpark.context import get_active_session
import pandas as pd

#session = get_active_session()
st.title("Customer Feedback with Skip Logic")

# 1. Standard question (Must be outside st.form for skip logic to work)
cust_id = st.text_input("Customer ID")
ease = st.radio("2. How easy is it to use our platform?", 
                ["Very Easy", "Somewhat Easy", "Neutral", "Difficult"], index=None)

# SKIP LOGIC: If "Difficult", skip to improvements. Otherwise, show more questions.
if ease != "Difficult":
    quality = st.selectbox("3. Rate service quality:", ["Excellent", "Good", "Average", "Poor"])
    variety = st.radio("4. Are you satisfied with variety?", ["Yes", "Mostly", "No"])
    # ... add other questions (5-7) here ...
    recommend = st.slider("7. Likelihood to recommend (1-10)", 1, 10, 8)
    
    # Initialize skipped values for the final table
    improvements = st.text_area("9. What is one thing we could do to improve?")
else:
    # If they selected "Difficult", these variables must still exist to save to the table
    st.info("Skipping to improvement suggestions...")
    quality = "N/A"
    variety = "N/A"
    recommend = 0
    improvements = st.text_area("9. Since you found it difficult, what specific improvement would help most?")

comments = st.text_area("10. Additional comments")

# Final Manual Submit Button
if st.button("Submit Survey"):
    if not cust_id:
        st.warning("Please enter your Customer ID.")
    else:
        # Prepare data for Snowflake
        df = pd.DataFrame([{
            "CUSTOMER_ID": cust_id,
            "EASE_OF_USE": ease,
            "SERVICE_QUALITY": quality,
            "PRODUCT_VARIETY": variety,
            "RECOMMEND_LIKELIHOOD": recommend,
            "IMPROVEMENT_SUGGESTIONS": improvements,
            "ADDITIONAL_COMMENTS": comments
        }])
        
        session.write_pandas(df, "CUSTOMER_SURVEY_RESULTS", overwrite=False)
        st.success("Feedback submitted!")
