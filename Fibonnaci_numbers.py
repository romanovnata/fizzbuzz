n = int(input("how many Fibonnaci numbers to generate: "))

fib = []
for i in range(0,n):
    if i < 2 :
        fib.append(1)
    else:
        fib.append(fib[i - 1] + fib[i - 2])
print(fib)
