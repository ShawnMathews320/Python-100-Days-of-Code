from turtle import Turtle, home
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):  # write the score on the screen
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):  # end game
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)

    def increment_score(self):  # add one to score
        self.clear()
        self.score += 1  
        self.update_scoreboard()      
