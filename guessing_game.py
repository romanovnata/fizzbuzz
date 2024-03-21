import random
def round():
    guess = random.randint(1, 9)
    print("Guess the number from 1 to 9.")
    counter = 0
    running = True
    while running == True:
        counter += 1
        usinput = int(input())
        if usinput > guess:
            print("Too high! Try again!")
        elif usinput < guess:
            print("Too low! Try again!")
        else:
            print("Congratulations! It took %d attempts" % counter)
            running = False

usinput = ""
while usinput != "exit":
    round()
    usinput = input("Type exit to quit or press Enter to play again: ")
