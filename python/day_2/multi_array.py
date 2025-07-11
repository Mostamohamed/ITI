x=int(input("enter your number: "))
result=[]
for i in range(1, x+1):
    m=[]
    for j in range(1,i+1) :
        m.append(i*j)
    result.append(m)

print(result)
        