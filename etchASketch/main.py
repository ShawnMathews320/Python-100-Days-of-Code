from turtle import Turtle, Screen

myTurtle = Turtle()
screen = Screen()
screen.colormode(255)
colorList = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120)]

def moveForward():
    myTurtle.forward(10)

def moveBackward():
    myTurtle.backward(10)

def moveAngleLeft():
    myTurtle.left(5)

def moveAngleRight():
    myTurtle.right(5)

screen.onkeypress(moveForward, "w")
screen.onkeypress(moveBackward, "s")
screen.onkeypress(moveAngleLeft, "a")
screen.onkeypress(moveAngleRight, "d")
screen.listen()

screen.exitonclick()