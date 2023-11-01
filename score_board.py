from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = None
        self.add_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def add_score(self):
        if self.score == None:
            self.penup()
            self.hideturtle()
            self.color("white")
            self.score = 0
        else:
            self.score += 1
            self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


