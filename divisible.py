number = int(input("Enter the number: "))
divisor = int(input("Enter divisor: "))

if number % divisor == 0: 
    print(str(number) + " is divisible by " + str(divisor) + " !")
else: 
    print(str(number) + " is not divisible by " + str(divisor) + " !")