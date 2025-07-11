name=input("enter your name : ")
while not name or name.isdigit():
    print("invalid please try again ")
    name=input("enter your name : ").strip()

email=input("enter your email : ")

while '@' in email and '.' in email and '.'not in email[0] and '@' not in email[0] and '.'not in email[-1] and '@' not in email[-1]:
    at_pos=email.find('@')
    dot_pos=email.find('.',at_pos)
    if dot_pos - at_pos ==1 or at_pos - dot_pos  ==1 or dot_pos < at_pos:
        print("invalid email")
        email=input("enter your email : ")
    elif  dot_pos > at_pos and  dot_pos- at_pos -1 >=3:
        print("valid email")
        break
