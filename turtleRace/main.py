from turtle import Turtle, Screen

import random

screen = Screen()
colorList = ["red", "orange", "yellow", "green", "blue", "purple"]  # colors for turtles
moveForwardList = [0, 2, 3, 4, 5, 6, 7, 8]  # how far our turtles can move each turn
yPos = 0  # where our first turtle's y axis will be
userWinningColor = screen.textinput("Make your bet", "Who will win the race? Enter a color "
"(options are red, orange, yellow, green, blue, purple):")  # see which turtle user thinks will win
isRacing = True

for i in range(6):  # set attributes for each turtle
    myTurtle = Turtle()
    myTurtle.penup()
    myTurtle.shape("turtle")
    myTurtle.color(colorList[i])
    myTurtle.goto(-300, yPos)
    yPos += 40

while isRacing:  # race still going on
    for turtle in screen.turtles():  # every turtle we created
        turtle.forward(random.choice(moveForwardList))  # give turtle random distance to move forward
        if turtle.xcor() > (300):  # finish line for turtles to reach
            actualWinningColor = turtle.color()[0]  # turtle color that won
            if userWinningColor == actualWinningColor:
                print(f"You won! The {userWinningColor} turtle is the winner")
            else:
                print(f"You lost. The {actualWinningColor} turtle is the winner")
                
            isRacing = False  # stop racing because turtle reached end
            break  

screen.bye()
screen.exitonclick()