numbers = list(range(0,23))
letters = ["T","R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
ID_number = input("Please enter the ID number to check its corresponding NIF letter: ")
while len(ID_number) > 8 or not ID_number.isdigit():
    print("Incorrect values. Remember that an ID number contains at most 8 numbers. Try again.")
    ID_number = input("Please enter the ID number to check its corresponding NIF letter: ")
result = int(ID_number) % 23
for i in numbers:
    if result == i:
        print(f"The corresponding NIF is {ID_number}-{letters[i]}")
