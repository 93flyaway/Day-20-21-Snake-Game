from turtle import Turtle
SCOREBOARD_POSITION = (0, 280)
ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.color("white")
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_screen()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_screen()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
