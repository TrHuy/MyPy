import turtle
import math
wn = turtle.Screen()
wn.bgcolor("lightgreen")
# wn.setworldcoordinates(-20, -20, 300, 300)
emma = turtle.Turtle()
emma.pensize(3)
d = {"blue" : 1, "red" : 2, "yellow" : 3, "gray" : 4, "pink" : 5}


def square(length):
    for i in d:
        for j in range(4):
            emma.forward(length * d[i])
            emma.left(90)
        emma.right(135)
        emma.up()
        emma.forward(length/math.sqrt(2))
        emma.left(135)
        emma.down()
        emma.color(i)


square(30)
wn.exitonclick()