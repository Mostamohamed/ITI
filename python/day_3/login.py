database=[
    {"username": "mostafa", "password": "1234"},
    {"username": "salman", "password": "abc"},
    {"username": "abdo", "password": "123"}
]

check1=False
check2=False
check3=False
check4=False

username=input("enter your username : ")
password=input("enter your password : ")

for user in database:
    if user["username"] == username and user["password"] != password:
        check1 = True
        break
    elif user["username"] != username and user["password"] == password:
        check2 = True
        break
    elif user["username"] != username and user["password"] != password:
        check3 = True
        break
    else :
        check4 = True
        break

if check1 == True:
     print("Invalid password.")
elif check2 == True:
     print("Invalid username.")
elif check3 == True:
     print("Invalid username and password.")
else :
    print("Login successful!")