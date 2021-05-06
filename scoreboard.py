from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.level = 1
        self.penup()
        self.goto(x=-245, y=270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):

        self.write(f'Level {self.level}', align=ALIGNMENT, font=FONT)

    def increase_level(self):

        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):

        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
