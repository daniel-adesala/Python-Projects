import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.player_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()

    cars.create_car()
    cars.move_cars()

    #Detect when the turtle player collides with a car 
    #and stop the game if this happens. If you get stuck, check the video walkthrough in Step 5.
    for car in cars.allcars:
      if car.distance(player) < 20:
         game_is_on = False
         score.game_over()
    

    #Detect when the turtle player has reached the top edge of the 
    # screen (i.e., reached the FINISH_LINE_Y). When this happens, 
    # return the turtle to the starting position and increase the speed of the cars. 
    # Hint: think about creating an attribute and using the MOVE_INCREMENT
    #to increase the car speed. If you get stuck, check the video walkthrough in Step 6

    if player.ycor() == 280:
       player.next_level()
       cars.increase_car_speed()
       score.update()



screen.exitonclick()
