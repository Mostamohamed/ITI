numbers = [1, 2, 3, 4, 5]
categorized_numbers = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(categorized_numbers)

print("   ")
print("/////////////////////////////////////////////////////////")
print("   ")

numbers = [1, 2, 3, 4, 5]
categorized_numbers = [( num if num % 2 == 0 else "Odd") for num in numbers]
print(categorized_numbers)
print(type(categorized_numbers))
