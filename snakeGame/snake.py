from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20,0), (-40, 0)]  # where the snake segments will start


class Snake:

    def __init__(self) -> None:
        self.segments = []  # add snake segments here after they are created
        self.createSnake()
        self.head = self.segments[0] 

    def createSnake(self):
        for position in STARTING_POSITIONS:  # create the snake with as many segments as there are positions in the startingPositions list
            self.add_segment(position)

    def add_segment(self, position):  # find position to add segment to 
        newSnakeSegment = Turtle("square")
        newSnakeSegment.color("white")
        newSnakeSegment.penup()  # so our snake won't draw
        newSnakeSegment.goto(position)
        self.segments.append(newSnakeSegment)  # add segment to list

    def extend(self):  # add new segment to snake
        self.add_segment(self.segments[-1].position())  # get position of last segment in list

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):  # iterate through segments list
            # send each segment to the next segment in the list's position so the segments will follow one another
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.head.forward(MOVE_DISTANCE)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)