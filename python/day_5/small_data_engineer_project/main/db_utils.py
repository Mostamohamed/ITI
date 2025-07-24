import pyodbc

# Database connection
def get_connection():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"
        "Database=EmailDB;"
        "Trusted_Connection=yes;"
    )

# Check if email exists
def email_exists(cursor, email):
    cursor.execute("SELECT 1 FROM EmailValidation WHERE email = ?", email)
    return cursor.fetchone() is not None

# Insert emails into the DB
def insert_emails_to_db(emails, is_valid):
    conn = get_connection()
    cursor = conn.cursor()
    inserted_count = 0

    for email in emails:
        if not email_exists(cursor, email):
            cursor.execute(
                "INSERT INTO EmailValidation (email, is_valid) VALUES (?, ?)",
                email, is_valid
            )
            inserted_count += 1

    conn.commit()
    conn.close()
