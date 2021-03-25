import random
class Date:
    def __init__(self, day, month, year):
        daysInMonth = [31,29,31,30,31,30,31,31,30,31,30,31]
        if day not in range(1, daysInMonth[month - 1] + 1):
            self.day = random.randint(1, daysInMonth[month - 1])
        else: 
            self.day = day
        
        if month not in range(1, len(daysInMonth)+1):
            self.month = random.randint(1,len(daysInMonth))
        else:
            self.month = month
        self.year = year
        
    def printInfo(self):
        print(str(self.day) + "-" + str(self.month) + "-" + str(self.year))
            
class Subject:
    name = 'Programming'
    semester = 1
    dates = []
    def __init__(self, name, semester, dates):
        self.name = name
        self.semester = semester
        self.dates = dates
            
    def printInfo(self):
        print("Name:", self.name)
        print("Semester:", self.semester)
        print("Dates:\n")
        for i in self.dates:
            i.printInfo()
        