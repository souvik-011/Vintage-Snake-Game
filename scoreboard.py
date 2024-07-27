from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align="center", font=("arial", 14, "normal"))
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", move=False, align="center", font=("arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align="center", font=("arial", 14, "normal"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.score_update()

    def increase_score(self):
        self.score += 1
        self.score_update()
