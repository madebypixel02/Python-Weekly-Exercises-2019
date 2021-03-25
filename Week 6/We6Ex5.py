import random
numbers = []
lucky_number = int(input("Enter a number between 1 and 100, and I'll try to find it: "))
for i in range(1, 101):
    random_number = random.randint(1, 100)
    while numbers.count(random_number) >= 1:
        random_number = random.randint(1, 100)
    numbers.append(random_number)
for item in numbers:
    if item == lucky_number:
        print(f"Got it! Your number was {item}. It took me {numbers.index(item) + 1} attempts to figure it out.")
if lucky_number not in numbers:
    print("Couldn't find your number... Wait! I see what's going on, your number is not between 1 and 100!")