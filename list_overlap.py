import random
def randomlist():
    lenth = random.randint(5, 10)
    list = []
    for i in range(1, lenth):
        r = random.randint(1, 5)
        list.append(r)
    return list

a = randomlist()
b = randomlist()

result = []
for element in a:
    if element in b and element not in result:
        result.append(element)
print("For two given lists:")        
print(a)
print(b)
print("Here is intersection: " + str(result))        