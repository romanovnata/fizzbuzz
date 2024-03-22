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
new_list = [x for x in a for y in b if x==y]
result = []
for x in new_list:
    if x not in result: 
        result.append(x)
print("For list: " + str(a))
print("and list:: " + str(b))
print("overlap is following: "+ str(result))