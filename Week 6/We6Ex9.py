sentence = input("Enter your sentence: ")
characters = ()
for i in sentence:
    while not i in characters:
        characters += (i,)
print(characters)
