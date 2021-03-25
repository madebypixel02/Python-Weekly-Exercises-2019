age = int(input("Please enter you age: "))
ticket_price = 9
if age <= 5:
    ticket_price -= ticket_price * 0.6
    print("A ticket for children will cost: ", ticket_price, "euros.")
elif age >= 60:
    ticket_price -= ticket_price * 0.55
    print("A ticket for the elderly will cost: ", ticket_price, "euros.")
elif 5 < age <= 26:
    ticket_price -= ticket_price * 0.2
    print("A ticket for young people will cost: ", ticket_price, "euros.")
else:
    print("Your age doesn't get any discounts, sorry!. You must pay", ticket_price, "euros.")