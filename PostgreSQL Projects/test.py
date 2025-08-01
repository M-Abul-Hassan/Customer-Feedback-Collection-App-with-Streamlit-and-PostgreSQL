import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection
engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/feedback_db")

# Set up session
Session = sessionmaker(bind=engine)

# Insert feedback
def insert_feedback(name, email, message):
    with Session() as session:
        session.execute(
            text('INSERT INTO "Table" (name, email, message, submitted_at) VALUES (:name, :email, :message, NOW())'),
            {"name": name, "email": email, "message": message}
        )
        session.commit()

# Load feedback
def load_feedback():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT name, email, message, submitted_at FROM "Table" ORDER BY submitted_at DESC'))
        return pd.DataFrame(result.fetchall(), columns=result.keys())

# Streamlit UI
st.title("📋 Customer Feedback App")

with st.form("feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    message = st.text_area("Your Feedback")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and email and message:
            insert_feedback(name, email, message)
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please fill in all fields.")

# Display stored feedback
st.write("---")
st.subheader("📊 Submitted Feedback")

feedback_df = load_feedback()
if not feedback_df.empty:
    st.dataframe(feedback_df)
else:
    st.info("No feedback submitted yet.")
