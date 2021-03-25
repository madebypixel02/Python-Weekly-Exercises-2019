import classes
import random
dates = []
counter = random.randint(1,7)
while counter <= 30:
    date = classes.Date(counter, 11, 2019)
    dates.append(date)
    counter += 7
subject1 = classes.Subject('Programming', 1, dates)
subject1.printInfo()
