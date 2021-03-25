import random
list1 = []
for i in range(1, 21):
    list1.append(random.randint(1, 9))

usr_number = int(input("Please enter a number between 1 and 9: "))
while usr_number not in range(1, 10):
    print("Number isn't valid. Try again.")
    usr_number = int(input("Please enter a number between 1 and 9: "))
print(f"\nList is {list1}")
if usr_number not in list1:
    print(f"Sorry, number {usr_number} was not found in the list. Better luck next time!")
for item in list1:
    if usr_number == item:
        print(f"The number you chose, {usr_number}, is in the list. Its index is {list1.index(item)}")
        list1[list1.index(item)] = None

