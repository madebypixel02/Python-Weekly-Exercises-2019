import random
def del_duplicated(list1, list2):
    output = []
    for number in list2:
        list1.append(number)
    for item in list1:
        if item not in output:
            output.append(item)
    return output

list1 = list(range(1,7))
list2 = list(range(4,10))
print("List 1 :", list1)
print("List 2 :", list2)
output = del_duplicated(list1, list2)
print("Output:", output)