# Exercise 1
class Player:
    def __init__(self, name, lastName, age, position, team):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.position = position
        self.team = team
        
    def printStats(self):
        print("\n---------------STATS---------------")
        print(self.name, self.lastName, "is", self.age, "years old. He plays", self.position, "in", self.team)
        
        