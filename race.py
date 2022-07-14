from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle Race", prompt="Pls enter your bet turtle: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
distance = [0, 30, 60, 90, 120, 150]

turtle_list = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    turtle_list.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-200, y=-70 + distance[i])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 200:
            is_race_on = False
            print(f"The winner is {turtle.pencolor()} turtle!")
            if user_bet == turtle.pencolor():
                print("You win the game! YEAH!")
            else:
                print("OH OH. You got it wrong...")
        else:
            turtle.forward(random.randint(0, 50))



screen.exitonclick()
