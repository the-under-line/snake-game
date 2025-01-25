from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.sety(260)

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, condition):
        if condition:
            self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=("Courier", 30, "normal"))
