from art import logo, vs
from data import data

import random
import os

currentScore = 0

def getOptions():  # get two options to compare
    randomNumber1 = random.randrange(len(data))
    randomNumber2 = random.randrange(len(data))

    while randomNumber2 == randomNumber1:  # we dont want to compare the same number so generate a number until it is different
        randomNumber2 = random.randrange(len(data))
    
    return data[randomNumber1], data[randomNumber2]

def getMostFollowers(object1, object2):
    if object1['follower_count'] > object2['follower_count']:
        return 'A'
    else:
        return 'B'

while True:
    object1, object2 = getOptions()  # get two options

    print(logo)
    if currentScore:  # means the user has a score above 0
        print(f"That's right! Current score: {currentScore}")

    print(f"Compare A: {object1['name']}, a {object1['description']}, from {object1['country']}.")  # show first option

    print(vs)

    print(f"Against B: {object2['name']}, a {object2['description']}, from {object2['country']}.")  # show second option
    userGuessMostFollowers = input("Who has more followers? Type 'A' or 'B': ")  # ask user who has more followers
    actualMostFollowers = getMostFollowers(object1, object2)  # get the result

    if userGuessMostFollowers == actualMostFollowers:  # means user guessed correctly
        currentScore += 1  # add 1 to user score
        os.system('cls')  # clear console
    else:
        print(f"Sorry, that's wrong. Final score: {currentScore}")  # user guessed incorrectly so end the game
        break