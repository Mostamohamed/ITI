import requests
import random

valid_domains = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com"]
fake_domains = ["com", "fake", "123", "", ".com", "invalid@"]

def fetch_emails():
    emails = []
    response = requests.get("https://randomuser.me/api/?results=1000")
    if response.status_code == 200:
        users = response.json()['results']
        for user in users:
            target = user['email'].split('@')[0]

            if random.random() < 0.7:
                domain = random.choice(valid_domains)
                email = f"{target}@{domain}"
            else:
                choice = random.randint(1, 3)
                if choice == 1:
                    email = f"{target}outlook.com"
                elif choice == 2:
                    email = f"{target}@{random.choice(fake_domains)}"
                else:
                    email = str(random.randint(1000, 99999))
            emails.append(email)
    else:
        print("API Error")
    return emails
