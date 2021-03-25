welcm_msg = '''
Welcome
--------------------
1- Deposit
2- Withdraw
3- Exit'''
withdraw_msg = '''
Withdrawal
--------------------'''
deposit_msg = '''
Deposit
--------------------'''
exit_msg = '''
Exit
--------------------'''
usr_amount = 15000
usr_pin = 1234
attempts = 3
choice = int(input(f"{welcm_msg}\nChoose the operation you would like to perform: "))

while choice != 1 and choice != 2 and choice != 3:
    print("\nDidn't catch that. Try again.")
    choice = int(input(f"{welcm_msg}\nChoose the operation you would like to perform: "))

if choice == 1:
    input_amount_deposit = float(input(f"{deposit_msg}\nEnter the amount you wish to deposit: "))
    usr_amount += input_amount_deposit
    print(f"{deposit_msg}\nYou have a total of {usr_amount}€ after your deposit.")

elif choice == 2:
    input_amount_withdraw = float(input(f"{withdraw_msg}\nEnter the amount you wish to withdraw: "))
    while input_amount_withdraw > usr_amount:
        print(f"{withdraw_msg}\nYou don't have enough money. Try again.")
        input_amount_withdraw = float(input("Enter the amount you wish to withdraw: "))


    print(f"{withdraw_msg}\nRemaining attempts:", attempts)
    input_pin = int(input("Please confirm your PIN code: "))
    while input_pin != usr_pin:
        attempts -= 1
        if attempts == 0:
            print(f"{withdraw_msg}\n3 failed attempts!")
            break
        if len(str(input_pin)) != 4:
            print(f"{withdraw_msg}\nA PIN has four numbers, try again.")
        print("Remaining attempts:", attempts)
        input_pin = int(input("Please confirm your PIN code: "))
    if input_pin == usr_pin:
        print(f"{withdraw_msg}\nHere you go, {input_amount_withdraw}€. Enjoy!")
        usr_amount -= input_amount_withdraw
        print(f"Your balance is now {usr_amount}€.")
    else:
        print("Goodbye!")
elif choice == 3:
    print(f"{exit_msg}\nCome back again if you wish to deposit or withdraw money. Have a great day!")


