sentence = input("Enter your sentence: ")
characters = ()
for i in sentence:
    if i != " ":
        characters += (i,)
print(characters)