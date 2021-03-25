usr_amount = 15000
usr_pin = 1234
attempts = 3
input_amount = float(input("Welcome! Please enter the amount you would like to withdraw: " ))

while input_amount > usr_amount:
    print("You don't have enough money. Try again.")
    input_amount = float(input("Please enter the amount you would like to withdraw: "))

print("Remaining attempts:", attempts)
input_pin = int(input("Please confirm your PIN code: "))
while input_pin != usr_pin:
    attempts -= 1
    if attempts == 0:
        print("3 failed attempts!")
        break
    if len(str(input_pin)) != 4:
        print("A PIN has four numbers, try again.")
    print("Remaining attempts:", attempts)
    input_pin = int(input("Please confirm your PIN code: "))
if input_pin == usr_pin:
    print(f"Here you go, {input_amount}€. Enjoy!")
else:
    print("Goodbye!")