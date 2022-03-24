from art import logo

import os
import random

def getFirstCards():  # give the player and computer starting cards
    print(logo)
    playerList, computerList = [], []  # empty lists for cards

    # get user's and computer's starting cards
    playerHand1, playerHand2, computerHand1, computerHand2 = random.randrange(1, 12), random.randrange(1, 12), random.randrange(1, 12), random.randrange(1, 12)

    # if 11 is too great then turn it into a one
    if playerHand1 or playerHand2 == 11:
        if playerHand1 + playerHand2 > 21:
            playerHand1 = 1

    # add values to lists
    playerList.append(playerHand1)
    playerList.append(playerHand2)
    computerList.append(computerHand1)
    computerList.append(computerHand2)

    return playerList, computerList

def appendCard():  # adds a card to player's list
    playerSum = 0
    playerCardAdd = random.randrange(1, 12)
    
    for i in playerList:
        playerSum += i
    
    # if 11 is too great then turn it into a one
    if playerCardAdd == 11 and playerCardAdd + playerSum > 21:
        playerCardAdd = 1
        playerSum += 1
    else:
        playerSum += playerCardAdd

    playerList.append(playerCardAdd)

    return playerSum

def computeWinner():  # see who won the game
    playerSum = 0
    computerSum = 0

    for i in playerList:
        playerSum += i
    for i in computerList:
        computerSum += i
    
    if playerSum <= 21:  # player is in valid range of card score
        if playerSum == computerSum:  # player and computer got the same score
            print("You Tied!")
        elif playerSum > computerSum:  # player scored higher
            print("You Won!")
        else:  # computer scored higher
            print("You Lost!")
    else:  # player busted so they lost
        print("You Lost!")

startGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")  # ask user if they want to play

if startGame == 'y':  # player wants to play so start game
    playerList, computerList = getFirstCards()  # get lists of randomly generated cards

    while startGame == 'y':
        # see if user wants to keep going or stop
        hitOrPass = input(f"Your cards: {playerList}\nComputer's first card: {computerList[0]}\nType 'y' to get another card, type 'n' to pass: ")

        if hitOrPass == 'y':  # player wants to keep going so add another card
            playerSum = appendCard()
            if playerSum > 21:  # player is out of valid range so end game and tell them they lost
                print("You Bust! (your scored passed 21)")

                # game ended see if player wants to play again
                startGame = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
                if startGame == 'y':
                    os.system("cls")
                    playerList, computerList = getFirstCards()
        else:
            print(f"Your final hand: {playerList}\nComputer's final hand: {computerList}")  # show cards in each hand
            computeWinner()  # show the results of game

            # game ended see if player wants to play again
            startGame = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
            if startGame == 'y':
                os.system("cls")
                playerList, computerList = getFirstCards()