var1 = "What's up?"
var2 = var1
print(var2)

# Result is: What's up?


var1 = "Let's hang out!"
print(var2)

# Again, result is: What's up?
# This is because var2 was assigned the initial value of var1. Changing the value of var1 doesn't modify the value of var2, unless you reassign var2 = var1 after changing the value of var1.