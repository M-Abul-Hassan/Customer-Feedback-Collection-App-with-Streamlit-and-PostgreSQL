# 📋 Customer Feedback Collection App with Streamlit and PostgreSQL

This is a simple web-based app for collecting customer feedback using **Streamlit** and storing it in a **PostgreSQL database** managed through **PgAdmin 4**. It allows users to submit feedback (name, email, message) and view all previous submissions.

---

## 🚀 Features

- 🧾 Submit name, email, and feedback via a clean form.
- 💾 Store submissions in PostgreSQL using SQLAlchemy and psycopg2.
- 📊 Display all feedback entries in real-time within the app.
- 🖥️ Easily view and manage records via PgAdmin 4.

---

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit
- PostgreSQL + PgAdmin 4
- SQLAlchemy
- Psycopg2
- Pandas

---

## 🪜 How to Run This Project Locally

### ✅ 1. Install Python & pip

Make sure Python 3.8 or above is installed. You can download it from:

> [https://www.python.org/downloads](https://www.python.org/downloads)

---

### ✅ 2. Install PostgreSQL and PgAdmin

Download PostgreSQL from:

> [https://www.postgresql.org/download](https://www.postgresql.org/download)

During installation, note down the password you set for the **postgres** user (e.g., `12345`).

---

### ✅ 3. Create the Database and Table

1. Open **PgAdmin 4**
2. Create a new database:
   - Name: `feedback_db`
3. Create a table named `feedback` with the following schema:

| Column Name   | Data Type                | Constraint              |
|---------------|--------------------------|--------------------------|
| id            | serial                   | Primary Key             |
| name          | character varying        | Not Null                |
| email         | character varying        | Not Null                |
| message       | text                     | Not Null                |
| submitted_at  | timestamp (default now())| Default: `NOW()`        |

---

### ✅ 4. Set Up the Project

```bash
# Create project folder and virtual environment
mkdir feedback_app
cd feedback_app
python -m venv venv
venv\Scripts\activate    # For Windows
# source venv/bin/activate  # For Mac/Linux

