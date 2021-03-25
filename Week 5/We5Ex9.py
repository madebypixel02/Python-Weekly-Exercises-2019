def is_perfect(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total = total + i
    return total == number

number = int(input("Please Enter any Number to calculate the perfect numbers in it: "))
for n in range(1, number +1):
    if is_perfect(n):
        print(f"{n} is a perfect number.")
