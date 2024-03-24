import random
def randomlist():
    lenth = random.randint(5, 10)
    list = []
    for i in range(1, lenth):
        r = random.randint(1, 5)
        list.append(r)
    return list

a = randomlist()
print(a)
b = [a[0], a[-1]]
print(b)