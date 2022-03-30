# import colorgram

# colorsList = []
# colors = colorgram.extract('image.jpg', 26)

# for color in colors:  # generate list of colors
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     newColor = (r, g, b)
#     colorsList.append(newColor)

from turtle import Turtle, Screen

import random

myTurtle = Turtle()
myTurtle.shape("turtle")
myTurtle.speed("normal")
screen = Screen()
screen.colormode(255)
colorList = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120)]
yPos = 0

for row in range(10):
    for col in range(10):
        myTurtle.pendown()
        myTurtle.dot(10, random.choice(colorList))
        myTurtle.penup()
        myTurtle.forward(25)

    yPos += 25    
    myTurtle.goto(0, yPos)

myTurtle.hideturtle()
screen.exitonclick()