from email_generator import fetch_emails
from email_validator import split_emails
from file_utils import load_existing_emails, save_emails

# Step 1: Fetch emails
emails = fetch_emails()

# Step 2: Validate
valid, invalid = split_emails(emails)

# Step 3: Load existing
existing_valid = load_existing_emails("V2/data/valid_emails.csv")
existing_invalid = load_existing_emails("V2/data/invalid_emails.csv")

# Step 4: Filter duplicates
new_valid = [e for e in valid if e.lower() not in existing_valid]
new_invalid = [e for e in invalid if e.lower() not in existing_invalid]

# Step 5: Save results
save_emails("V2/data/valid_emails.csv", new_valid)
save_emails("V2/data/invalid_emails.csv", new_invalid)

print(f"✅ Done. Added {len(new_valid)} valid and {len(new_invalid)} invalid emails.")
