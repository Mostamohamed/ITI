import csv

with open(r'C:\Users\mosta\Desktop\ITI\python\day6\sheet.csv', newline='') as file:
    reader = csv.reader(file)
    data=[]
    for row in reader:
        data.append(row)

emails=[]
for i in range (1,len(data)):
    emails.append(data[i][3])
# print(emails)



def is_valid_email(email):
    if (
        '#' not in email and
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


valid_emails = list(filter(is_valid_email, emails))
print(valid_emails)


domain=[]

for email in valid_emails:
    domain.append(email.split('@')[1])

print(len(domain))

set_of_domains = set(domain)
print(set_of_domains)

print(len(set_of_domains))




import json
domain_dict = {
    str(i + 1): {"domain": domain}
    for i, domain in enumerate(sorted(set_of_domains))
}

with open("email_domains.json", "w") as f:
    json.dump(domain_dict, f, indent=4)