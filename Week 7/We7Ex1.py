def extend(matrix):
    matrix_extended = []
    for a in matrix:
        for b in a:
            matrix_extended.append(b)
    return matrix_extended


matrix1 = []
rows1 = int(input("Let's create a matrix! Enter the number of rows you want: "))
cols1 = int(input("Got it. Now enter the number of columns you want: "))


# Building matrix 1
for i in range(rows1):
    temp = []
    for p in range(cols1):
        usr_number = int(input(f"Enter a value for the ({i},{p}) position: "))
        temp.append(usr_number)
    matrix1.append(temp)

# Printing matrix 1
print("Matrix 1 is now:\n")
for item in matrix1:
    for element in item:
        print(element, end= " ")
    print()

matrix2 = []
rows2 = int(input("\nLet's create another matrix. Enter the number of rows you want: "))
cols2 = int(input("Got it. Now enter the number of columns you want: "))


# Building matrix 2
for i in range(rows2):
    temp = []
    for p in range(cols2):
        usr_number = int(input(f"Enter a value for the ({i},{p}) position: "))
        temp.append(usr_number)
    matrix2.append(temp)

# Printing matrix 2
print("Matrix 2 is now:\n")
for item in matrix2:
    for element in item:
        print(element, end= " ")
    print()

matrix1_extended = extend(matrix1)
matrix2_extended = extend(matrix2)
print()
for number in matrix1_extended:
    if number in matrix2_extended:
        print(f"{number} has been found in both matrices.")
