def randomize(min_bound = 0, max_bound = 1, is_int = False):
    import random
    if is_int:
        random_result = random.randint(int(min_bound), int(max_bound))
    else:
        random_result = random.uniform(float(min_bound), float(max_bound))
    return random_result

# Example of execution 1
print(randomize(5, 20, False))

# Example of execution 2
print(randomize(2, 5, True))

# Example of execution 3
print(randomize())