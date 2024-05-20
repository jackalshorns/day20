from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.ht()
        self.penup()
        self.color('white')
        self.setpos(0,270)
        self.update_scoreboard()


    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score} ", False, align='center', font=('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER, MAN!", False, align='center', font=('Arial', 24, 'normal'))