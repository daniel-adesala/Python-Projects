from turtle import Turtle

class Scoreboard(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        with open("highscore.txt") as hs:
             self.highscore = int(hs.read())
        self.hideturtle()
        self.color("black") 
        self.penup()
        self.goto(-320, 250)
        self.scoreboard()
        

    def scoreboard(self): 
        self.clear()
        self.write(f"HIGHSCORE = {self.highscore}                           SCORE = {self.score}/50", move= False,  align= 'left', font=("Courier", 15, "bold"))


    def update_score(self):
        self.score += 1
        self.scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", move= False,  align= 'center', font=("Courier", 20, "bold"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode = "w") as hs:
              hs.write(f"{self.highscore}")
        self.score = 0
        self.scoreboard()
            


          
        
        


    

