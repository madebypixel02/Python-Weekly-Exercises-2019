def range2(stop, start = 0, step = 1):
    output = range(start, stop, step)
    return output

# Examples of execution:
print(list(range2(21)))
print(list(range2(21, 15)))
print(list(range2(21, 0, 5)))
