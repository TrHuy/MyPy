import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

emma = turtle.Turtle()
emma.color("blue")
emma.pensize(0)
emma.speed(0)
def circle():
    for i in range(360):
        emma.forward(1)
        emma.left(1)

