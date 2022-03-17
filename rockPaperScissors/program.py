import random

roundsLeft = 3
roundWinner = ""
userScore = 0
computerScore = 0

while roundsLeft > 0:
    userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
    computerChoice = int(random.randint(0,2))  # random number between 0, 1, and 2

    if userChoice == computerChoice:
        print("The user and computer chose the same option!")
    else:
        if userChoice == 0:
            userSymbol = "Rock"
        elif userChoice == 1:
            userSymbol = "Paper"
        elif userChoice == 2:
            userSymbol = "Scissors"

        if computerChoice == 0:
            computerSymbol = "Rock"
        elif computerChoice == 1:
            computerSymbol = "Paper"
        elif computerChoice == 2:
            computerSymbol = "Scissors"

        if userChoice == 0 and computerChoice == 1:  # user picked rock, computer picked paper
            computerScore += 1  # computer won
            roundWinner = "computer"
        elif userChoice == 1 and computerChoice == 0:  # user picked paper, computer picked rock
            userScore += 1  # user won
            roundWinner = "user"
        elif userChoice == 0 and computerChoice == 2:  # user picked rock, computer picked scissors
            userScore += 1  # user won
            roundWinner = "user"
        elif userChoice == 2 and computerChoice == 0:  # user picked scissors, computer picked rock
            computerScore += 1  # computer won
            roundWinner = "computer"
        elif userChoice == 1 and computerChoice == 2:  # user picked paper, computer picked scissors
            computerScore += 1
            roundWinner = "computer"
        elif userChoice == 2 and computerChoice == 1:  # user picked scissors, computer picked paper
            userScore += 1
            roundWinner = "user"
        
        print("You chose: " + userSymbol + "\nThe computer chose: " + computerSymbol + f"\nThe {roundWinner} won this round")
        
        if roundsLeft == 1:
            if userScore > computerScore:
                print("You have won!")
            elif userScore < computerScore:
                print("Oh no! You lost to the computer.")
            

        roundsLeft -= 1  # one less round because it is not a stalemate