import classes
name = input("Enter your name: ")
lastName = input("Enter your last name: ")
programming = int(input("Enter your programming grade: "))
algebra = int(input("Enter your algebra grade: "))
calculus = int(input("Enter your calculs grade: "))
physics = int(input("Enter your physics grade: "))
writing = int(input("Enter your writing grade: "))


student1 = classes.Student(name, lastName, programming, algebra, calculus, physics, writing)
student1.printInfo()