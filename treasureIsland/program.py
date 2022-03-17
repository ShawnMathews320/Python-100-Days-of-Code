import random

generateLeftOrRight = random.randint(0,1) 

# first question about which crossroads to take
crossroad = input('Welcome to treasure island.\nYour mission is to find the treasure.\nYou are at a cross road. Where do you want to go? Type "left" or "right\n')

if crossroad == "left":
    lakePath = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')

    if lakePath == "wait":
        doorPath = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
        if doorPath == "red":
            print("You get electrocuted and die as soon as you grab the door handle. Game Over.")
        if doorPath == "blue":
            print("An armed shotgun trap shoots you as soon as you open the door. Game Over")
        if doorPath == "yellow":
            print("Coins pour out of the door as it opens and you see all of the treasure. You Win!")
    elif crossroad == "swim":
        print("Before you could reach the other side you were ripped apart by sharks. Game Over")
if crossroad == "right":
    print("You were swallowed whole by a giant snake. Game Over")