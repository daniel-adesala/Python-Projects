from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#Create a turtle player that starts at the bottom of the screen and listen for the "Up"
# keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
    def player_up(self):
        self.fd(MOVE_DISTANCE)

     #Detect when the turtle player has reached the top edge of the 
    # screen (i.e., reached the FINISH_LINE_Y). When this happens, 
    
    
    def next_level(self):
        self.goto(STARTING_POSITION)