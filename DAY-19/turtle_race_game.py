import turtle
from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)

colors = ["red","orange","yellow","green","blue","purple"]

# tim = Turtle(shape="turtle")
# tim.color("red")
# tim.penup()
# tim.goto(x=-230,y=-100)
#
# to = Turtle(shape="turtle")
# to.color("orange")
# to.penup()
# to.goto(x=-230,y=-70)
#
# m = Turtle(shape="turtle")
# m.color("yellow")
# m.penup()
# m.goto(x=-230,y=-40)
#
# i = Turtle(shape="turtle")
# i.color("green")
# i.penup()
# i.goto(x=-230,y=-10)
#
# ti = Turtle(shape="turtle")
# ti.color("blue")
# ti.penup()
# ti.goto(x=-230,y=20)
#
# t = Turtle(shape="turtle")
# t.color("purple")
# t.penup()
# t.goto(x=-230,y=50)


# maim's
y_position = -90
all_turtles= []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_position)
    y_position += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print(f"You've win! the {winning_color} turtle is winner")
            else :
                print(f"You've lost! the {winning_color} turtle is winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()