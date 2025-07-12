emails = [
    "user1@gmail.com",         
    "user2@yahoo.com",         
    "user3@.com",              
    "user4outlook.com",        
    "user5@icloud",            
    "@hotmail.com",            
    "user6@protonmail.com",    
    "user7@aol..com",          
    "user8@mail.com",          
    "user9@live.com.",         
]

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

def check_emails(email_list):
    for email in email_list:
        result = "valid" if is_valid_email(email) else "invalid"
        print(f"{email} → {result} email")


check_emails(emails)


valid_emails = list(filter(is_valid_email, emails))
domains = list(map(lambda email: email.split('@')[1], valid_emails))
print("Valid emails:", valid_emails)
print("Extracted domains:", domains)
