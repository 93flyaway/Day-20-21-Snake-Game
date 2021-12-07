from turtle import Turtle
SCOREBOARD_POSITION = (0, 280)
ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.color("white")
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_screen()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
