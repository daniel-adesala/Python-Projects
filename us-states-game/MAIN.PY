 
import turtle, pandas, scoreboard
import time
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
print(turtle.screensize())
ans = turtle.Turtle()
ans.hideturtle()
ans.color("black")
ans.penup()
score = scoreboard.Scoreboard()
data = pandas.read_csv("50_states.csv")

mentionedstates = []

game_on = True
while game_on :
    answer_state = screen.textinput(title="Guess the State", prompt = "What's another state's name? :").title()
    print(answer_state)
    
    if answer_state == "Exit":
        missingstates = [state for state in data.state if state not in mentionedstates]
        new_data = pandas.DataFrame(missingstates)
        new_data.to_csv("states_to_learn.csv")
        break

    
    if len(mentionedstates) == 50:
        ans.home()
        ans.write(f"Bravo! \nYou've listed all 50 states \n Congratulations", move= False,  align= 'center', font=("Courier", 9, "bold"))
        game_on = False

    elif answer_state in mentionedstates:   
        continue_ = screen.textinput(title="double mention", prompt = "You've mentioned this state already!! (click 'OK' to continue)").capitalize()

    elif answer_state in data.state.to_string(index = False):
          for cor in data.state:        
           if cor == answer_state:
              mentionedstates.append(answer_state)
              row = data[data.state == answer_state]
              x = int(row.x.to_string(index = False))
              y = int(row.y.to_string(index = False))
              ans.goto(x,y)
              ans.write(f"{answer_state}", move= False,  align= 'center', font=("Courier", 9, "normal"))
              score.update_score()
  
    else:
        game_on = False
        score.reset()
        score.game_over()
        







screen.exitonclick()