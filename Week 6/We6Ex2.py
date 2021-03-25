import random
numbers = list(range(1,21))
randomized = []
for i in numbers:
    randomized.append(random.choice(numbers))
print(randomized)
print(f"Possible numbers: {len(randomized)}")

list2 = randomized
randomized[0] = True
print(list2[0])
# We made a live copy of randomized in the list we called list2. Therefore, modifying anything from the first list will modify the second one, without having to reassign one list to the other.