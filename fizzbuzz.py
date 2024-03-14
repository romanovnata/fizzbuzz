def fizzbuzz_check(n):
    if (n % 3) == 0 and (n % 5) == 0:
        print("fizzbuzz") 
    elif (n % 3) == 0:
        print("fizz")
    elif (n % 5) == 0:
        print("buzz")
    else:
        print(n)

print("Enter number")
while True:
    x = input()
    if x == "q":
        print("Your game is over")
        break
    fizzbuzz_check(int(x))
# print(x)