import streamlit as st
import psycopg2
from sqlalchemy import create_engine, text
import pandas as pd

# Database connection string
db_url = "postgresql+psycopg2://postgres:12345@localhost:5432/feedback_db"

# Create SQLAlchemy engine
engine = create_engine(db_url)

# Insert feedback into the "Table"
def insert_feedback(name, email, message):
    with engine.connect() as conn:
        conn.execute(
            text('INSERT INTO "Table" (name, email, message, submitted_at) VALUES (:name, :email, :message, NOW())'),
            {"name": name, "email": email, "message": message}
        )

# Load feedback from the "Table"
def load_feedback():
    with engine.connect() as conn:
        result = conn.execute(
            text('SELECT name, email, message, submitted_at FROM "Table" ORDER BY submitted_at DESC')
        )
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

st.write("---")
st.subheader("📊 Submitted Feedback")

feedback_df = load_feedback()

if not feedback_df.empty:
    st.dataframe(feedback_df)
else:
    st.info("No feedback submitted yet.")
