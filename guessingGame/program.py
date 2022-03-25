import random
from art import logo

print(logo)

userDifficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty: Type 'easy' or 'hard': ")
randomNumber = random.randrange(1, 101)  # get random number for user

if userDifficulty == 'easy':
    attempts = 10
elif userDifficulty == 'hard':
    attempts = 5

while attempts > 0:
    userGuess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
    attempts -= 1

    if userGuess > randomNumber:
        print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
    elif userGuess < randomNumber:
        print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
    else:
        print(f"You got it! The answer was {userGuess}")
        break