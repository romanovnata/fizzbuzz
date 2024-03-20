# Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game
def round():
    print("Round")
    player1_choice = input("player 1 choise:")
    player2_choice = input("player 2 choise:")
    if player1_choice == "scissors":
        if player2_choice == "rock":
            print("Player 2 wins!")
        elif player2_choice == "paper":
            print("Player 1 wins!")
        elif player2_choice == "scissors":
            print("draw")
        else:
            print("Player 2 wrong input")
    elif player1_choice == "paper":
        if player2_choice == "rock":
            print("Player 1 wins!")
        elif player2_choice == "paper":
            print("draw")
        elif player2_choice == "scissors":
            print("Player 2 wins!")
        else:
            print("Player 2 wrong input")
    elif player1_choice == "rock":
        if player2_choice == "rock":
            print("draw")
        elif player2_choice == "paper":
            print("Player 2 wins!")
        elif player2_choice == "scissors":
            print("Player 1 wins!")
        else:
            print("Player 2 wrong input")
    else:
        print("Player 1 wrong input")

####################################################    
userinput = "yes"
while userinput == "yes":
    round() 
    userinput = input("Would you like to play again? ")