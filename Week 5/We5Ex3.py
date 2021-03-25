import random
attempts = 1
magic_number = random.randint(1,20)
usr_number = int(input("Guess the number I'm thinking of, it's between 1 and 20: "))
while usr_number not in range(1,21):
    print("Your number isn't between 1 and 20!")
    usr_number = int(input("Guess again: "))
    attempts += 1
while magic_number != usr_number:
    if usr_number > magic_number:
        print(usr_number, "is larger than the number I'm thinking of.")
    elif usr_number < magic_number:
        print(usr_number, "is smaller than the number I'm thinking of.")
    usr_number = int(input("Guess again: "))
    attempts += 1
if attempts == 1:
    print(f"\nWOW, you figured out the number I was thinking of on the first try! You should probably go buy lottery tickets now :)")
else:
    print(f"Congrats! It took you {attempts} attempts to find the number I was thinking of!")
