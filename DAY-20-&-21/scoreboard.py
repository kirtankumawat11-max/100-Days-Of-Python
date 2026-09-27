from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-10, 270)
        self.write(f"Score : {self.score}", True, align=ALIGNMENT, font=FONT )

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()