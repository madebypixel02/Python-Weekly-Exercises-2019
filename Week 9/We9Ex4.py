def string_fix(string):
    string = list(string)
    string[0] = string[0].upper()
    for i in range(len(string)):
        if string[i] == "i" and string[i - 1] == " " and string[i + 1] == " ":
            string[i] = string[i].upper()
        if (string[i] == "." or string[i] == "!" or string[i] == "?" or string[i] == "...") and string[i] != string[-1]:
            string[i + 2] = string[i + 2].upper()

    return string

sentence = input("Enter the lowercase sentence(s): ")
fixed_string = string_fix(sentence)
for item in fixed_string:
    print(item, end = "")
