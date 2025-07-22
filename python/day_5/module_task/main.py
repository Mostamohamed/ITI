import my_utils

# find letter i 
text = input("Enter a string: ")
my_utils.find_string(text)

# build sample mario  
x=int(input("enter number :"))
my_utils.sample_mario(x)

# muli_table until the given number
n=int(input("enter your number: "))
my_utils.m_table(n)

# # number of vowles letters
word = input("Enter your word : ")
my_utils.nvowles(word)

# # sort
arr=[]
print("enter 5 numbers to sort : ")
for i in range(5):
    x=int(input(f"Number {i+1}:"))
    arr.append(x) 
# sort array ascending 
my_utils.sort_ascending(arr)
# sort array descending 
my_utils.sort_descending(arr)

# # mario using list 
x = int(input("Enter number: "))
my_utils.mario_list(x)

# mario using list 
x = int(input("Enter number: "))
my_utils.m_table_list(x)

#check user name function
user=input("enter your name : ")
my_utils.user_check(user)

# login function 
username=input("enter your username : ")
password=input("enter your password : ")
my_utils.check_login(username,password)


# email validate
email = input("Enter your email: ")
my_utils.email_validate(email)

