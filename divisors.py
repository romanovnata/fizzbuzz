# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
x = int(input("Enter the number: "))
div = []
a = range(1, (x + 1))
for i in a:
    if x % i == 0:
        div.append(i)
print(str(x) + " has following divisors: " + str(div)) 