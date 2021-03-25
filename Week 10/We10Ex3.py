# Count function:
def count(list1, x = 0):
    counter = 0
    for item in list1:
        if item == x:
            counter += 1
    return counter

# Index function:
def index(list1, x):
    counter = 0
    if x not in list1:
        return -1
    for item in list1:
        if item != x:
            counter += 1
        else:
            return counter

# Append function:
def append(list1, x):
    list1 += [x,]
    return list1

# Insert function:
def insert(list1, x, index):
    output = []
    for i in range(len(list1)):
        if i == index:
            output += [x,]
        output += [list1[i],]
    return output

# Remove function:
def remove(list1, x):
    output = []
    for item in list1:
        if item != x:
            output += [item,]
        else:
            x = None
    return output

# removeAll function:
def removeAll(list1, x):
    output = []
    for item in list1:
        if item != x:
            output += [item,]
    return output

# Clear function:
def clear(list1):
    list1 = []
    return list1

# Pop function:
def pop(list1):
    output = []
    for i in range(len(list1)):
        if list1[i] != list1[-1]:
            output += [list1[i],]
        else:
            last_value = list1[i]
    return output, last_value