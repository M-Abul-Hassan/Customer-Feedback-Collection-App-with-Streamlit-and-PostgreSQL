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



# 🗃️ How to Create Database, Tables, and Columns in PgAdmin 4

This guide walks you through the steps to create a PostgreSQL database, a table, and columns using the **PgAdmin 4** graphical interface.

---

## 🟢 Step 1: Open PgAdmin 4

- Launch **PgAdmin 4**
- Enter your **PostgreSQL master password** (e.g., `12345`)

---

## 🏗️ Step 2: Create a New Database

1. In the left panel, right-click on **Databases**
2. Select **Create > Database**
3. In the popup:
   - **Database Name**: `feedback_db`
   - Leave other settings as default
4. Click **Save**

✅ Your database `feedback_db` is now created.

---

## 📋 Step 3: Create a Table

1. Navigate to:

Servers > PostgreSQL > Databases > feedback_db > Schemas > public > Tables



2. Right-click on **Tables**
3. Select **Create > Table**
4. Under the **General** tab:
- **Name**: `feedback` (or `Table` if you want it capitalized)

5. Switch to the **Columns** tab
6. Add the following columns:

| Column Name   | Data Type   | Nullable | Default  | Notes                        |
|---------------|-------------|----------|----------|------------------------------|
| `id`          | `serial`    | ❌ No     | —        | Set as Primary Key (click the key icon) |
| `name`        | `varchar`   | ❌ No     | —        |                              |
| `email`       | `varchar`   | ❌ No     | —        |                              |
| `message`     | `text`      | ❌ No     | —        |                              |
| `submitted_at`| `timestamp` | ✅ Yes    | `now()`  | Automatically sets submission time |

7. Click **Save**

✅ The `feedback` table with required columns is created successfully.

---

## 👀 Step 4: View or Edit Data

1. Right-click on the `feedback` table
2. Select **View/Edit Data > All Rows**
3. A table view will open showing all rows submitted (e.g., from your Streamlit app)

This is where your submitted form data will appear in real time.

---

> 💡 **Tip**: You can also create this table using raw SQL queries if you prefer.

