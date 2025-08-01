import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# --- PostgreSQL connection settings ---
DATABASE_URL = "postgresql+psycopg2://postgres:12345@localhost:5432/feedback_db"

# Create SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# --- Insert feedback into PostgreSQL ---
def insert_feedback(name, email, message):
    try:
        with Session() as session:
            session.execute(
                text('''
                    INSERT INTO "Table" (name, email, message, submitted_at)
                    VALUES (:name, :email, :message, NOW())
                '''),
                {"name": name, "email": email, "message": message}
            )
            session.commit()
    except Exception as e:
        st.error(f"Error saving feedback: {e}")

# --- Load all feedback entries from database ---
def load_feedback():
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text('SELECT name, email, message, submitted_at FROM "Table" ORDER BY submitted_at DESC')
            )
            return pd.DataFrame(result.fetchall(), columns=result.keys())
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# --- Streamlit UI ---
st.title("📋 Customer Feedback App")

with st.form("feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Feedback")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and email and message:
            insert_feedback(name, email, message)
            st.success("✅ Thank you for your feedback!")
        else:
            st.warning("⚠️ Please fill in all fields before submitting.")

# --- Display feedback ---
st.write("---")
st.subheader("📊 Submitted Feedback")

feedback_df = load_feedback()

if not feedback_df.empty:
    st.dataframe(feedback_df)
else:
    st.info("No feedback submitted yet.")
