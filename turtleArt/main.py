from dis import dis
import random
from turtle import Turtle, Screen

myTurtle = Turtle()
colors = ["deep pink", "dark orange", "medium spring green", "blue", "saddle brown", "deep sky blue"]
directions = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)

# for i in range(20):  # draw dashed line
#     myTurtle.pendown()
#     myTurtle.forward(7)
#     myTurtle.penup()
#     myTurtle.forward(7)

# successively print shapes in the range of i
# for i in range(3, 11):  # i is number of sides of shapes
#     angle = 360/i
#     distance = 40
#     randomColorIndex = random.randrange(len(colors))
#     myTurtle.pencolor(colors[randomColorIndex])
#     for x in range(i):
#         myTurtle.right(angle)
#         myTurtle.forward(distance)
#     distance += 40

# myTurtle.pensize(7)
myTurtle.speed('fastest')

# for i in range(100):  # draws a random path for turtle to walk
#     randomDirection = random.randrange(4)
#     myTurtle.pencolor((random.randrange(256), random.randrange(256), random.randrange(256)))   
#     myTurtle.setheading(random.choice(directions))
#     myTurtle.forward(20)

for i in range(360//10):  # spiral of circles
    myTurtle.circle(50)
    myTurtle.pencolor((random.randrange(256), random.randrange(256), random.randrange(256)))
    myTurtle.setheading(myTurtle.heading() + 10)
    myTurtle.circle(50)

screen.exitonclick()