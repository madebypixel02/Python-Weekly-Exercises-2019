def createListNumbers():
    import random
    numbers = []
    even_numbers = list(range(0,101,2))
    for i in range(10):
        numbers.append(random.choice(even_numbers))
    total = 0
    for i in numbers:
        total += i
    max_numbers = max(numbers)
    min_numbers = min(numbers)
    mean = total/10

    return numbers, max_numbers, min_numbers, mean

print(createListNumbers())
