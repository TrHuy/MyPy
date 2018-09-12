import turtle
import math
wn = turtle.Screen()
wn.bgcolor("lightgreen")
# wn.setworldcoordinates(-20, -20, 300, 300)
emma = turtle.Turtle()
emma.pensize(2)
emma.speed(0)
emma.color("blue")


for i in range(1, 250, 2):
    emma.right(90.5)
    emma.forward(i)


wn.exitonclick()