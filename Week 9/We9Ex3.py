def euro_convert(amount = 0, currency = 'dollar'):
    if currency == 'dollar':
        converted = amount * 1.11
    elif currency == 'yen':
        converted = amount * 120.99
    elif currency == 'pound':
        converted = amount * 0.86
    else:
        return 'ERROR: INVALID CURRENCY'
    return converted

amount = float(input("Enter the amount of Euros you would like to convert: "))
currency = input("Got it. Enter the currency you would like to covert your money to (pound, dollar, yen): ").lower()
if currency != 'dollar' and currency != 'pound' and currency != 'yen':
    currency = ""
print()
print("Your conversion is:", end = "\n")
print(f"{amount}€ -> {euro_convert(amount, currency)} {currency}")
