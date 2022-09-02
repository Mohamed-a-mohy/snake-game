from turtle import Turtle

score = 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.ht()
        self.write(f"Score = {score}", False, align="center")

    def end_game(self):
        self.goto(0, 0)
        self.write(f"Game over", False, align="center")


    def score_edit(self):
        global score
        score += 1
        self.clear()
        self.write(f"Score = {score}", False, align="center")



