import random
rows = random.randint(1,4)
cols = random.randint(2,6)

matrix = []
for i in range(rows):
    temp = []
    total = 0
    for j in range(cols - 1):
        random_number = random.randint(1,20)
        temp.append(random_number)
        total += random_number
    temp.append(total)
    print(f"Added {total} to the matrix")
    matrix.append(temp)
print("\nMatrix is now:", end = "\n")
for item in matrix:
    for element in item:
        print(element, end= " ")
    print()


