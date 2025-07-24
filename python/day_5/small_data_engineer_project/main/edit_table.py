import pyodbc

# Connect
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=EmailDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()


cursor.execute("""
    ALTER TABLE EmailValidation
    ADD CONSTRAINT unique_email UNIQUE (email);
""")
print("edit success")
conn.commit()
conn.close()