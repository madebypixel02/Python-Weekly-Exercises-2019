list1 = [1, 2, 3, 4, 5]
list1[0] = list1[-1]
print(list1[0])
print(list1[-1])
# Both results are 5.

list1[-1] = True
print(list1[0])
print(list1[-1])
# Now list1[0] is still 5, but list1[-1] is now True. This is because changing the value of list1[-1] does not change the value of list1[0].

list1[0] = "Hi"
print(list1[0])
print(list1[-1])
# Again, each index modification does not make much difference, even though we stated that list1[0] = list1[-1]. We would need to rewrite this line in order to update the value of list1[0] to the value in list1[-1].
# Result is now is "Hi" for list1[0] and True for list1[-1]