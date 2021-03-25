name = 'Johnny Depp'
age = 55
height = 178
weight = 65.4
eyes = 'Brown'
hair = 'Brown'
print("Let’s talk about %s." %name)
print("He’s %i centimeters tall." %height)
print("He’s %f kilograms heavy." %weight)
print("Actually that’s not too heavy.")
print("He has %s eyes and %s hair." % (eyes, hair))

## Result is:
# Let’s talk about Johnny Depp.
# He’s 178 centimeters tall.
# He’s 65.400000 kilograms heavy.
# Actually that’s not too heavy.
# He has Brown eyes and Brown hair.##



print("Let’s talk about", name)
print("He’s", height, "centimeters tall.")
print("He’s", weight, "kilograms heavy.")
print("Actually that’s not too heavy.")
print("He has", eyes, "eyes and", hair, "hair.")

## Result is:
# Let’s talk about Johnny Depp
# He’s 178 centimeters tall.
# He’s 65.4 kilograms heavy.
# Actually that’s not too heavy.
# He has Brown eyes and Brown hair.##

# As we can see, we had to split the strings to add each variable in the correct place. Both results are nearly the same.