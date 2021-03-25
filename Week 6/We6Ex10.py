import random
def maximum(tuple1):
    current_max = 0
    for item in tuple1:
        if item > current_max:
            current_max = item
    return current_max

def minimum(tuple1):
    import sys
    current_min = sys.maxsize
    for item in tuple1:
        if item < current_min:
            current_min = item
    return current_min

scores = ()
for i in range(1,6):
    random_score = random.randint(1,10)
    while random_score in scores:
        random_score = random.randint(1, 10)
    scores += (random_score,)
print(f"The lowest score is {minimum(scores)}, and the highest score is {maximum(scores)}", end = "\n\n")
for judge in range(1,6):
    print(f"Judge {judge} gave the gymnast {scores[judge - 1]} points.")
