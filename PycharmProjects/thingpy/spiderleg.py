import turtle
from circleturtle import circle
import math
wn = turtle.Screen()
wn.bgcolor("lightgreen")

emma = turtle.Turtle()
emma.color("blue")
emma.pensize(1)
emma.speed(0)

def spider(length, nleg):
    for size in range(nleg):
        emma.forward(length)
        emma.forward(-length)
        emma.right(360/nleg)
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(i)
        emma.color("blue")
        emma.right(90)
        emma.forward(length//10)
        emma.left(90)
        emma.color("brown")
        c = 2 * i * math.pi * (length//10)

        for j in range(360):
            emma.forward(c/360)
            emma.left(1)


spider(300, 36)
turtle.done()
