NTRY = 5

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


while NTRY != 0:
    try:
        email = input("Enter your email: ")

        if email.isdigit():
            raise ValueError("Email cannot be just a number!")

        if is_valid_email(email):
            print("Email is valid.")
            break
        else:
            NTRY -= 1
            print(f"Invalid email. Attempts left: {NTRY}")

    except Exception as e:
        NTRY -= 1
        print(f"Error: {e}. Attempts left: {NTRY}")

if NTRY > 0:
    print("Success!")
else:
    raise("App is closing.")
