# find letter i 
def find_string(text):
    index = 0
    for i in text:
        if i == 'i':
            print('in index : ',index)
        index += 1
        
# build sample mario       
def sample_mario(x):
    for i in range(1, x + 1):
        print(" " * (x - i) + "*"* i)
        
        
# muli_table until the given number
def m_table(x):
    for i in range(1, x+1):
       for j in range(1,i+1) :
            print(f"{i}*{j}={i*j}")
            

# number of vowles letters
def nvowles(letter):
    number = 0
    for i in letter:
        if i =="a" or i =="e" or i =="i" or i =="o" or i =="u":
            number+=1
    print("number of vowles letters",number)
    
# sort array ascending 
def sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return print("sort ascending : ",arr)

# sort array descending 
def sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return print("sort descending : ",arr)

# mario using list
def mario_list(x):
    l = [" "]*x
    for i in range(1, x + 1):
        l[-i] = "*"
        print(l)

    
# muli_table until the given number with but every group in a list alone
def m_table_list(x):
    result=[]
    for i in range(1, x+1):
        m=[]
        for j in range(1,i+1) :
            m.append(i*j)
        result.append(m)
    print(result)
  

# check username function
def user_check(user):
    while not user or user.isdigit():
        print("invalid please try again ")
        user=input("enter your name : ").strip()
    print(f"Welcome, {user}!")
    return user
# login function

#import database from database file
from user_database import database

def check_login(username, password):
    for user in database:
        if user["username"] == username and user["password"] != password:
            print("Invalid password.")
            break
        elif user["username"] != username and user["password"] == password:
            print("Invalid username.")
            break
        elif user["username"] != username and user["password"] != password:
            print("Invalid username and password.")
            break
        else :
            print("Login successful!")
            break


#email validate

def email_validate(email):
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
            if email.isdigit():
                NTRY -= 1
                print(f"Email cannot be just a number!. Attempts left: {NTRY}")
                email = input("Enter your email: ")
                
            if is_valid_email(email):
                print("Email is valid.")
                break
            else:
                NTRY -= 1
                print(f"Invalid email. Attempts left: {NTRY}")
                email = input("Enter your email: ")
                

        except Exception as e:
            NTRY -= 1
            print(f"Error: {e}. Attempts left: {NTRY}")

    if NTRY > 0:
        print("Success!")
    else:
        raise("App is closing.")