import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")


image= "Day25/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
#this function is for coordinates of mouse click. We can use it to get the coordinates of the mouse click on the screen. 


df=pd.read_csv("Day25/day-25-us-states-game-start/50_states.csv")
states_list = df["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state's name?").title()
    if answer_state=="Exit":
        break
    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        result=df[df["state"]==answer_state]
        t.goto(result["x"].item(),result["y"].item())
        t.pendown()
        t.write(answer_state)


#States to learn
with open("Day25/states_to_learn.csv",'w') as file:
    for states in states_list:
        if states not in guessed_states:
            file.write(f"{states}\n")
    

# turtle.mainloop() # keeps the window open
turtle.mainloop()

 
