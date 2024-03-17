number = int(input("Enter the number: "))
if number % 2 == 0: 
    print("This number is even!", end = " ")
    if number % 4 == 0:
        print("Also it is divisible by 4!")
else: 
    print("This number is odd!")
