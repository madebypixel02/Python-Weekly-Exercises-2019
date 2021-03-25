import random

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

A = int(input("Enter the first value: "))
B = int(input("Enter the second value: "))

while A + 5 >= B:
    print("Incorrect values for A and B. Remember that you must satisfy: A + 5 < B.")
    A = int(input("Enter the first value: "))
    B = int(input("Enter the second value: "))

even_numbers = []
odd_numbers = []
random_numbers = []
for i in range(1, 6):
    random_numbers.append(random.randint(A, B))
for item in random_numbers:
    if is_even(item):
        even_numbers.append(item)
    else:
        odd_numbers.append(item)
print(even_numbers)
print(odd_numbers)


if len(even_numbers) == 0:
    even_numbers.extend(odd_numbers)
elif len(even_numbers) == 1:
    even_numbers.extend(odd_numbers)
elif len(even_numbers) == 2:
    even_numbers.insert(1, odd_numbers[0])
    even_numbers.insert(3, odd_numbers[1])
    even_numbers.insert(5, odd_numbers[2])
elif len(even_numbers) == 3:
    even_numbers.insert(1, odd_numbers[0])
    even_numbers.insert(3, odd_numbers[1])
elif len(even_numbers) == 4:
    even_numbers.insert(1, odd_numbers[0])
print("Total:", even_numbers)