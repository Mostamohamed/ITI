x=int(input("enter your number: "))

for i in range(1, x+1):
    for j in range(1,i+1) :
        print(f"{i}*{j}={i*j}")