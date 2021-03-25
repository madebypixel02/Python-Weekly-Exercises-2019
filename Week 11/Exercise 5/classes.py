import random
class Dice:
    name = "Penguin"
    outcomes = list(range(1,7))
    def __init__(self, player_name = name, n_rolls = 3):
        self.rolls = []
        self.name = player_name
        self.n_rolls = n_rolls
        for i in range(self.n_rolls):
            self.rolls.append(random.choice(self.outcomes))
            
    def printInfo(self):
        print("Results for", self.name, "are", self.rolls)
        
    def getHighest(self):
        current_max = 0
        for i in self.rolls:
            if self.rolls.count(i) > current_max:
                current_max = self.rolls.count(i)
        return current_max
    
    @property
    def getRolls(self):
        return self.rolls
    


