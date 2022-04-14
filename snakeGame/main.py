from turtle import Turtle, Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

isPlaying = True  # user is playing game

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# keyboard input to move snake
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.listen()

while isPlaying:  # means game is still going on
    screen.update()
    time.sleep(.1)
    snake.move()

    # check if snake is within borders
    if snake.head.xcor() < 300 and snake.head.xcor() > -300 and snake.head.ycor() < 300 and snake.head.ycor() > -300:
        if snake.head.distance(food) < 15:  # how close the snake needs to get to eat the food
            food.relocate()  # put food at new location cause snake ate it
            snake.extend()  # grow snake after eating
            scoreboard.increment_score()  # add one to player score
        for segment in snake.segments[1:]:  # detect collision with tail
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                isPlaying = False
    else:  # end game cause snake is out of bounds
        scoreboard.game_over()
        isPlaying = False

screen.exitonclick()