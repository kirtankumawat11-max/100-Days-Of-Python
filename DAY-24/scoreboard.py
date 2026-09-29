from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = self.check_in_data() - mine
        # maim's
        with open("data.txt") as data :
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # mine
    # def check_in_data(self):
    #     with open("data.txt") as content :
    #         score = int(content.read())
    #         return score


    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def maintain_high_score(self):
        with open("data.txt",mode="w") as score:
            score.write(f"{self.high_score}")

    def reset(self):
        self.clear()
        if self.score > self.high_score :
            self.high_score = self.score
            # self.maintain_high_score() - mine
            # maim's
            with open("data.txt", mode="w") as data :
                data.write(f"{self.high_score}")
        self.score =0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
