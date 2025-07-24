
# 📧 Email Validation Pipeline with SQL Server and Python

This project demonstrates a simple data engineering pipeline in Python that fetches random emails, validates them, and stores the results in a SQL Server database. It includes:

- Email generation using a public API
- Email validation logic
- Storage of valid/invalid emails into a SQL Server table
- Duplicate prevention via a `UNIQUE` constraint

---

## 🔧 Project Structure

```
project/
│
├── create_database.py       # Creates the EmailDB database and EmailValidation table
├── edit_table.py            # Adds unique constraint to prevent duplicates
├── db_utils.py              # Database utilities: connect, insert, check existence
├── email_generator.py       # Fetches and creates random (valid/invalid) emails
├── email_validator.py       # Validates emails based on simple logic
├── pipeline.py              # Main pipeline that runs all components
└── README.md                # Project documentation
```

---

## ⚙️ Requirements

- Python 3.8+
- SQL Server (LocalDB or full SQL Server)
- ODBC Driver 17+ for SQL Server
- Python packages:
  - `pyodbc`
  - `requests`

Install dependencies using:

```bash
pip install pyodbc requests
```

---

## 🗃️ Database Setup

The database creation and setup are done in two steps:

1. **Run `create_database.py`**  
   - Creates the `EmailDB` database and `EmailValidation` table.

2. **Run `edit_table.py`**  
   - Adds a `UNIQUE` constraint to ensure email uniqueness.

---

## 🧠 How It Works

1. **Fetch Emails**  
   `email_generator.py` uses the [randomuser.me API](https://randomuser.me) to generate random emails and adds noise for invalid formats.

2. **Validate Emails**  
   `email_validator.py` contains logic to check if an email format is valid based on structure (`@`, `.`, etc.).

3. **Store in Database**  
   `db_utils.py` handles database insertion and checks for duplicates using SQL queries.

4. **Main Pipeline**  
   `pipeline.py` connects everything:
   - Fetch → Validate → Save

---

## ▶️ Run the Pipeline

```bash
python pipeline.py
```

This will:
- Fetch 1000 random emails
- Validate them
- Insert valid/invalid emails into SQL Server

You'll see a message like:

```
Done. Attempted to save 720 valid and 280 invalid emails to the database.
```

---

## 📊 Table Schema

```sql
CREATE TABLE EmailValidation (
    id INT IDENTITY(1,1) PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    is_valid BIT NOT NULL,
    CONSTRAINT unique_email UNIQUE (email)
);
```

- `id`: Auto-incrementing ID
- `email`: Email address
- `is_valid`: `1` if valid, `0` if invalid

---

## 💡 Future Ideas

- Add logging (using Python `logging` module)
- Use real email validation libraries like `email-validator`
- Extend to store timestamps
- Build a web interface for viewing data

---

## 🧑‍💻 Author

**Mostafa Mohamed**  
Python & Data Engineering Enthusiast

---

## 📄 License

This project is open-source and free to use.
