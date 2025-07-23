def is_valid_email(email):
    if (
        '@' in email and 
        '.' in email and 
        email[0] not in ('.', '@') and 
        email[-1] not in ('.', '@')
    ):
        at_pos = email.find('@')
        dot_pos = email.find('.', at_pos)

        if dot_pos - at_pos == 1 or at_pos - dot_pos == 1 or dot_pos < at_pos:
            return False
        elif dot_pos > at_pos and dot_pos - at_pos - 1 >= 3:
            return True
    return False

def split_emails(emails):
    valid = [e for e in emails if is_valid_email(e)]
    invalid = [e for e in emails if not is_valid_email(e)]
    return valid, invalid
