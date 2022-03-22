import os
import math

from art import logo

continueBidding = True  # determins if loop will keep running or not
highestBidderAmount = -math.inf  # starting low value for highest bid
highestBidderName = ""  # name of highest bidder
bidDictionary = {}  # holds each bidder name and the amount they bid

def updateDictionary():  # add key value pair to dictionary
    userName = input("Welcome to the silent auction program.\nWhat is your name?: ")
    userBid = int(input("What is your bid?: $"))
    continueBid = input("Are there any other bidders? Type 'yes' or 'no'.\n")  # see if there are more bidders
    
    bidDictionary.update({userName: userBid})  # update our dictionary
    return continueBid


while continueBidding:  # run the loop if there are still bidders to account for
    continueBid = updateDictionary()  # update dictionary and see if there are more bidders    

    if continueBid == "yes":  # set up console for next bidders
        os.system('cls')  # clear console
    else:
        for x, y in bidDictionary.items():  # looking each key value pair in dictionary
            if y > highestBidderAmount:  # see if current bidder value is greater than the old max value
                highestBidderName = x  # update with new max value

        print(f"The winner is {highestBidderName} with a bid of ${bidDictionary[highestBidderName]}.")  # show the winner
        continueBidding = False  # end loop bc no more bidders
