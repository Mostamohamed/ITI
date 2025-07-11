numbers=[]
print("enter 5 numbers to sort : ")
for i in range(5):
    x=int(input(f"Number {i+1}:"))
    numbers.append(x) 

print("Ascending order : ",sorted(numbers))
print("descending order : ",sorted(numbers,reverse=True))
