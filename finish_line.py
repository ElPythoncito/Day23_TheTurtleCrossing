from turtle import Turtle

logo = r"""
    ╔══════════════════════════╗
    ║ 🎨🎨🎨 EL PYTHONCITO 🐍🐍🐍🐍  ║
    ╚══════════════════════════╝               
"""

class FinishLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300,240)
        self.pensize(2)

    def one_line(self):
        self.pendown()
        self.forward(10)
        self.penup()
        self.forward(10)

    def draw_complete_line(self):
        for i in range(31):
            self.one_line()

    def draw_logo(self):
        self.goto(-330,225)
        self.write(f"{logo}", font=("Courier", 12, "normal"), align="left")
