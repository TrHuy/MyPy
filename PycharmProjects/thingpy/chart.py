import turtle

wn = turtle.Screen()
border = 100
xs = [48, 117, 200, 240, 160, 260, 220]
# wn.setworldcoordinates(0, 0, 20*len(xs)+border, max(xs)+border)
wn.setworldcoordinates(-border, -border, 40 * len(xs) + border, max(xs) + border)
emma = turtle.Turtle()
emma.color("green")
emma.pensize(2)
emma.fillcolor("red")
emma.speed(0)


def chart(length):
    emma.begin_fill()
    emma.left(90)
    emma.forward(length)
    emma.right(90)
    emma.write(length)
    emma.forward(30)
    emma.right(90)
    emma.forward(length)
    emma.left(90)
    emma.end_fill()


for i in xs:
    chart(i)

wn.exitonclick()
