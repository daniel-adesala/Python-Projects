from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#Create cars that are 20px high by 40px wide that are randomly generated along the y-axis 
#and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen
#(think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. 
#If you get stuck, check the video walkthrough in Step 4.


class CarManager():
    def __init__(self):
        self.allcars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
          new_car = Turtle()
          new_car.shape("square")
          new_car.shapesize(1, 2)
          new_car.penup()
          new_car.color(random.choice(COLORS))
          new_car.goto(300, random.randint(-250, 250))
          self.allcars.append(new_car)

    def move_cars(self):
        for car in self.allcars:
            car.backward(self.car_speed)

    # return the turtle to the starting position and increase the speed of the cars. 
    # Hint: think about creating an attribute and using the MOVE_INCREMENT
    #to increase the car speed. If you get stuck, check the video walkthrough in Step 6
    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
