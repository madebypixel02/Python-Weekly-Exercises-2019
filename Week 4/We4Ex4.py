int_1 = int(input("Please enter the first integer number: "))
int_2 = int(input("Please enter the second integer number: "))
while int_2 == 0:
    print("Cannot divide by zero. Try again")
    int_2 = int(input("Please enter the second integer number: "))
print(f"Solution: {int_1}/{int_2} = {int_1/int_2}")