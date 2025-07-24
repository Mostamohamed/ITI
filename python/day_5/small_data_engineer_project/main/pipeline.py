from email_generator import fetch_emails
from email_validator import split_emails
from db_utils import insert_emails_to_db

# Step 1: Fetch emails
emails = fetch_emails()

# Step 2: Validate
valid, invalid = split_emails(emails)


# Step 3: insert to database
insert_emails_to_db(valid, True)
insert_emails_to_db(invalid, False)

print(f"Done. Attempted to save {len(valid)} valid and {len(invalid)} invalid emails to the database.")
