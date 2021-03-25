a, b, c, d = 5, 3, 20, 20
c -= (a + 1)/b - 3 + a % b
d -= (a + 1)/(b + 3 - 4 * a) % b
print("c:", c)
print("d:", d)

# The result of c is 19, and the result of d is 17.428571428571427, because the way you arrange the parenthesis is very important. Just like in conventional math, python first solves parenthesis, then solves powers, products, divisions or the modulus, and lastly calculates additions and subtractions.