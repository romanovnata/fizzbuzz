def divs(n):
    return [c for c in range(1, n+1) if n % c == 0]
      
def is_prime(n):
    return not len(divs(n)) > 2
    
n = int(input("Write the number:\n"))
print("%d is %s prime" % (n, "" if is_prime(n) else "not"))

