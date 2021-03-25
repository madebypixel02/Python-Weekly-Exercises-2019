months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
month_choice = input("Select a number between 1 and 12: ")

while int(month_choice) != 0:
    while int(month_choice) not in range(1, 13):
        print("Your choice does not represent any months of the year. Try again.")
        month_choice = input("Select a number between 1 and 12: ")
    print("Month:", months[int(month_choice) - 1])
    month_choice = input("Select another number between 1 and 12. (Tip, enter 0 to exit): ")
print("\nSee you soon!")