from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(-220, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def keep_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
