def reverse(a):
    return " ".join(a[::-1])

result = (input ("Enter the long phrase:")).split()
result = reverse(result)
print(result)