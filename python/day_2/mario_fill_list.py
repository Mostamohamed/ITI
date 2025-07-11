l = [" ", " ", " ", " ", " "]

x = int(input("Enter number: "))
for i in range(1, x + 1):
    l[-i] = "*"
    print(l)
