from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0

        super().__init__()
        self.hideturtle()
        self.color("gold")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center", font=('Courier', 15, 'bold'))
    
    def refresh_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Courier', 15, 'bold'))
    
    def print_game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over! Your score is {self.score}", align="center", font=('Courier', 20, 'bold'))
