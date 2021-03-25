def randomize_pass():
    import random
    random_len = random.randint(7, 10)
    random_pass = []

    uppercase = []
    for i in range(65, 91):
        uppercase.append(chr(i))

    lowercase = []
    for i in range(97, 123):
        lowercase.append(chr(i))

    numbers = []
    for i in range(48, 58):
        numbers.append(chr(i))

    symbols = []
    for i in range(58, 65):
        symbols.append(chr(i))
    for i in range(33, 48):
        symbols.append(chr(i))

    upper_exists, number_exists, symbol_exists = False, False, False
    types = [lowercase, uppercase, numbers, symbols]
    for i in range(random_len):
        random_type = random.choice(types)
        random_pass.append(random.choice(random_type))
        if random_type == uppercase:
            upper_exists = True
        elif random_type == numbers:
            number_exists = True
        elif random_type == symbols:
            symbol_exists = True

    while not upper_exists:
        random_pass[random.randint(0, random_len-1)] = random.choice(uppercase)
        upper_exists = True
    while not symbol_exists:
        random_pass[random.randint(0, random_len-1)] = random.choice(symbols)
        symbol_exists = True
    while not number_exists:
        random_pass[random.randint(0, random_len-1)] = random.choice(numbers)
        number_exists = True


    # Returning the password
    return random_pass

# Printing a test of 5 random passwords
for j in range(5):
    print(f"Random Password {j + 1}: ", end="")
    random_pass_test = randomize_pass()
    for character in random_pass_test:
        print(character, end="")
    print()