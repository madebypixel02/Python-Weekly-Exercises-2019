import classes
usr_base = int(input("Enter size of the base of your triangle: "))
usr_height = int(input("Enter size of the height of your triangle: "))

triangle1 = classes.RightTriangle(usr_base, usr_height)
area = triangle1.getArea()
print(area)