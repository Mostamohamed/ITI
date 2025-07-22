import requests
import random
import os

#Step 1: Define Domains
valid_domains = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com"]
fake_domains = ["com", "fake", "123", "", ".com", "invalid@"]

emails = []

#Step 2: Fetch 1000 random users
response = requests.get("https://randomuser.me/api/?results=1000")
if response.status_code == 200:
    users = response.json()['results']

    for user in users:
        target = user['email'].split('@')[0]

        # 70% chance to generate valid email
        if random.random() < 0.7:
            domain = random.choice(valid_domains)
            email = f"{target}@{domain}"
        else:
            # 30% chance for invalid email
            choice = random.randint(1, 3)
            if choice == 1:
                email = f"{target}outlook.com"  # Missing @
            elif choice == 2:
                email = f"{target}@{random.choice(fake_domains)}"
            else:
                email = str(random.randint(1000, 99999))  # Just numbers
        emails.append(email)
else:
    print("API error")

#Step 3: Email Validation Function
def is_valid_email(email):
    if (
        '@' in email and 
        '.' in email and 
        email[0] != '.' and 
        email[0] != '@' and 
        email[-1] != '.' and 
        email[-1] != '@'
    ):
        at_pos = email.find('@')
        dot_pos = email.find('.', at_pos)

        if dot_pos - at_pos == 1 or at_pos - dot_pos == 1 or dot_pos < at_pos:
            return False
        elif dot_pos > at_pos and dot_pos - at_pos - 1 >= 3:
            return True
    return False

#Step 4: Split into Valid / Invalid Emails
valid_emails = [e for e in emails if is_valid_email(e)]
invalid_emails = [e for e in emails if not is_valid_email(e)]

#Step 5: Load Existing Emails from File
def load_existing_emails(filename):
    existing = set()
    if os.path.exists(filename):
        with open(filename, "r") as f:
            next(f, None)  # Skip header if exists
            for line in f:
                existing.add(line.strip().lower())
    return existing

existing_valid = load_existing_emails("valid_emails.csv")
existing_invalid = load_existing_emails("invalid_emails.csv")

#Step 6: Filter Out Duplicates 
new_valid = [email for email in valid_emails if email.lower() not in existing_valid]
new_invalid = [email for email in invalid_emails if email.lower() not in existing_invalid]

#Step 7: Write to CSV Files 
def save_emails(filename, emails):
    is_new_file = not os.path.exists(filename) or os.stat(filename).st_size == 0
    with open(filename, "a") as f:
        if is_new_file:
            f.write("email\n")
        for email in emails:
            f.write(email + "\n")

save_emails("valid_emails.csv", new_valid)
save_emails("invalid_emails.csv", new_invalid)

#Done
print(f"✅ Done. Added {len(new_valid)} new valid and {len(new_invalid)} new invalid emails.")
