word = input("Enter the string: ")
drow = word[::-1]
if drow == word:
    print("Your word is palindrome!")
else:
    print("Your word is not palindrome!")

