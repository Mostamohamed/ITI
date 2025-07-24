import pyodbc

# Connect to server
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"     
    "Trusted_Connection=yes;",
    autocommit=True
)

cursor = conn.cursor()

# Step 1: Create Database if not exists
cursor.execute("IF DB_ID('EmailDB') IS NULL CREATE DATABASE EmailDB;")
print("Database created successfully.")
conn.commit()

# Step 2: Reconnect to EmailDB
conn.close()
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=EmailDB;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Step 3: Create Table
cursor.execute("""
    IF OBJECT_ID('EmailValidation', 'U') IS NULL
    CREATE TABLE EmailValidation (
        id INT IDENTITY(1,1) PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        is_valid BIT NOT NULL
    );
""")
conn.commit()

print("table created successfully.")
conn.close()
