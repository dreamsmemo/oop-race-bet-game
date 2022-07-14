from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def clockwise():
    tim.circle(50, -50)

def counter_clockwise():
    tim.circle(50, 50)

def clear_drawing():
    tim.penup()
    tim.home()
    tim.clear()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="c", fun=clear_drawing)


screen.exitonclick()