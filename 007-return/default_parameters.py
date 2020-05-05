def greet(name, greeting="Hello"):
    return f"{greeting} {name}."


print(greet("marcel"))


def greet_complete(name, greeting_sentence="Hello *name*. I Hope you are well."):
    new_sentence = greeting_sentence.replace("*name*", name)
    return new_sentence


print(greet_complete("Lotte"))
print(greet_complete("Hank", "Hey *name*! How are you?"))
