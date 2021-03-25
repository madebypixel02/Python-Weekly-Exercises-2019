import classes
island1 = classes.Island('Mallorca',[[1,2], [3,5]], 'Spain', True)
island2 = classes.Island('Santa Clotilde',[[7,2], [19, -4]], 'Uranus', True)
passenger1 = classes.Passenger('Alejandro', '51260715-V', 'Z50V-23A')
passenger2 = classes.Passenger('María', '34234397-S', 'Z50V-23A')
passenger3 = classes.Passenger('Pedro', '69384738-T', 'Z50V-23A')
passengers = [passenger1, passenger2, passenger3]
plane1 = classes.Plane('Z50V-23A', island1, island2, passengers, 'Iberia')
plane1.fly()