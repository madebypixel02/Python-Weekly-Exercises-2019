class Student:
    def __init__(self, name, lastName, programming, algebra, calculus, physics, writing):
        self.name = name
        self.lastName = lastName
        self.programming = programming
        if self.programming not in range(1,11):
            self.programming = 0
        
        self.algebra = algebra
        if self.algebra not in range(1,11):
            self.algebra = 0
            
        self.calculus = calculus
        if self.calculus not in range(1,11):
            self.calculus = 0
        
        self.physics = physics
        if self.physics not in range(1,11):
            self.physics = 0
        
        self.writing = writing
        if self.writing not in range(1,11):
            self.writing = 0
        
    def printInfo(self):
        print("Grades for", self.name, self.lastName, "are:", self.programming, self.algebra ,self.calculus, self.physics, self.writing)
        

