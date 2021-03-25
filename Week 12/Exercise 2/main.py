import classes
import random
ran_size = random.randint(1, 10)
rectangles = []
square_exists = False
max_area = 0
max_perimeter = 0
max_side = 0
max_area_rectangle = None
max_perimeter_rectangle = None
max_side_rectangle = None
print("Random number of triangles:", ran_size)
print("Square Triangles:")
for i in range(ran_size):
    rectangle = classes.Rectangle(random.randint(1, 10), random.randint(1, 10))
    rectangles.append(rectangle)
for rectangle in rectangles:
    if rectangle.base == rectangle.height:
        print(rectangle.toString())
        square_exists = True
    if rectangle.area() >= max_area:
        max_area = rectangle.area()
        max_area_rectangle = rectangle
    if rectangle.perimeter() >= max_perimeter:
        max_perimeter = rectangle.perimeter()
        max_perimeter_rectangle = rectangle
    if rectangle.biggestSide() > max_side:
        max_side = rectangle.biggestSide()
        max_side_rectangle = rectangle
    
if not square_exists:
    print("No squares were generated, tough luck!")
print("Max area:", max_area_rectangle.toString())
print("Max perimeter:", max_perimeter_rectangle.toString())
print("Max side:", max_side_rectangle.toString())
square_max = max_side_rectangle.squarefy()
if square_max:
    square_max = classes.Rectangle(max_side, max_side)
    print("Base was changed,", square_max.toString())
elif not square_max:
    square_max = classes.Rectangle(max_side, max_side)
    print("Height was changed,", square_max.toString())
    