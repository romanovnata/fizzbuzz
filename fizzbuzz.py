def fizzbuzz_check(n):
    if (n % 3) == 0 and (n % 5) == 0:
        return "fizzbuzz" 
    elif (n % 3) == 0:
        return "fizz"
    elif (n % 5) == 0:
        return "buzz"
    else:
        return str(n)

print("Enter number")
while True:
    x = input()
    if x == "q":
        print("Your game is over")                
        break
    print(fizzbuzz_check(int(x)))
# print(x)