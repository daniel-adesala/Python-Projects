from turtle import Turtle
FONT = ("Courier", 24, "normal")
#Create a scoreboard that keeps track of which level the user is on. Every time the turtle player 
# does a successful crossing, the level should increase. When the turtle hits a car, 
# GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.
#
#
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.create_scoreboard()
        
    def create_scoreboard(self):  
        
        self.write(f"LEVEL = {self.score}", move= False,  align= 'left', font=FONT)
        
     
    def update(self):
        self.clear()
        self.score += 1
        self.create_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER",  align= 'center', font=FONT)





