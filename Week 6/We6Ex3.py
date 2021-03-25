import random
float_list = []
length = int(input("Enter the length of the list: "))
while length <= 0:
    print(f"Length {length} is not valid. Try again.")
    length = int(input("Enter the length of the list: "))
for item in range(1, length +1):
    float_list.append(random.randint(1, 49))
print(f"list is {float_list}")
for number in range(0, length):
    float_list[number] = int(float_list[number])
print(f"\nThe sum of all the entire parts is {sum(float_list)}")