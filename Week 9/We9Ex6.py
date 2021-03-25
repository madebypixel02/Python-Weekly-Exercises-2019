def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True

    else:
        return False
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
n_days = 0
usr_month = int(input("Let's see the number of days in a specific month. Enter a value from 1 to 12: "))
while usr_month not in range(1, 13):
    print("INVALID MONTH.")
    usr_month = int(input("Enter a value from 1 to 12: "))
usr_year = int(input("Enter a year: "))

if is_leap(usr_year) and usr_month == 2:
    n_days = 29
elif not is_leap(usr_year) and usr_month == 2:
    n_days = 28
elif usr_month == 1 or usr_month == 3 or usr_month == 5 or usr_month == 7 or usr_month == 8 or usr_month == 10 or usr_month == 12:
    n_days = 31
elif usr_month == 4 or usr_month == 6 or usr_month == 9 or usr_month == 11:
    n_days = 30


if usr_year == 2019:
    print(f"{months[usr_month - 1]} {usr_year} has {n_days} days.")
elif usr_year < 2019:
    print(f"{months[usr_month - 1]} {usr_year} had {n_days} days.")
else:
    print(f"{months[usr_month - 1]} {usr_year} will have {n_days} days.")

