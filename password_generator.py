import random
def weak():
    dictionary = ["fox", "dog", "cat", "caw", "bool"]
    first = random.choice(dictionary)
    second = random.choice(dictionary)
    return("".join([first, second]))

lowcase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowcase.upper()
numbers = "0123456789"
candidates = [lowcase, uppercase, numbers]
pass_lenght = 16
pass_raw = []
for i in range(0, pass_lenght):
    pass_raw.append()