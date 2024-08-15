import turtle
import pandas
import time
from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()
screen.setup(width=800,height=800)
screen.title("indian states")
image = "surya.gif"
screen.addshape(image)
Turtle(shape=image)

# input_state = screen.textinput(title="Guess the state of india ",prompt="what's the next state?").lower()

contents = pandas.read_csv("statesdata.csv")
states_list = contents["states"].tolist()
new_state_list = []
for _ in states_list:
    new_state_list.append(_.lower())
guessed_states = []

while len(guessed_states)<=28:

    input_state = screen.textinput(title=f"Guessed state is {len(guessed_states)}/28  ", prompt="what's the next state?").lower()
    if input_state in new_state_list:
        if input_state in guessed_states:
            tommy = Turtle()
            tommy.penup()
            tommy.hideturtle()
            tommy.goto(-100, 0)
            tommy.write("Already filled", font=("Arial", 30, "bold"))
            time.sleep(1)
            tommy.clear()

        if input_state not in guessed_states:
            guessed_states.append(input_state)

            contents[contents["states"].str.lower() == input_state]
            hold = contents[contents["states"].str.lower() == input_state]
            x = hold["x_cor"]
            y = hold["y_cor"]
            my_x = x.item()
            my_y = y.item()
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(x=my_x,y=my_y)
            turtle.dot(10)
            turtle.write(f"{input_state}",font=("Arial",12,"bold"))


    if input_state not in new_state_list:
          timmy = Turtle()
          timmy.penup()
          timmy.hideturtle()
          timmy.goto(-100,0)
          timmy.write("Wrong",font=("Arial",30,"bold"))
          time.sleep(1)
          timmy.clear()

    if len(guessed_states)==28:
        time.sleep(1)
        screen.bye()
    print(guessed_states)






screen.mainloop()


