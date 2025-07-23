import os

def load_existing_emails(filename):
    existing = set()
    if os.path.exists(filename):
        with open(filename, "r") as f:
            next(f, None)  # skip header
            for line in f:
                existing.add(line.strip().lower())
    return existing

def save_emails(filename, emails):
    is_new_file = not os.path.exists(filename) or os.stat(filename).st_size == 0
    with open(filename, "a") as f:
        if is_new_file:
            f.write("email\n")
        for email in emails:
            f.write(email + "\n")
