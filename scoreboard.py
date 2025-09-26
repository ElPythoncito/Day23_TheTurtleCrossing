from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(120, 250)
        self.draw_scoreboard()


    def draw_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=(FONT), align="left")

    def up_level_player(self):
        self.level += 1
        self.draw_scoreboard()

    def draw_game_over(self):
        self.draw_scoreboard()
        self.home()
        self.write(f"GAME OVER!!!", font=("Courier", 30, "bold"), align="center")
