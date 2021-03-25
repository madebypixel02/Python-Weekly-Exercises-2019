import classes
interval_count = int(input("Enter the number of intervals: "))
intervals = []
for i in range(interval_count):
    print("Interval:", i + 1)
    hour1 = int(input("Enter the starting hour of the interval: "))
    minute1 = int(input("Enter the starting minute of the interval: "))
    hour2 = int(input("Enter the ending hour of the interval: "))
    minute2 = int(input("Enter the ending minute of the interval: "))
    interval = classes.Time_interval(hour1, minute1, hour2, minute2)
    intervals.append(interval)
    print()
for i in intervals:
    i.printInfo()
    print("\n")
