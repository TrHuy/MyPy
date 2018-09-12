import turtle

wn = turtle.Screen()
wn.bgcolor("white")
t = turtle.Turtle()
t.color("red")
t.pensize(2)
print(type(t))
emma = turtle.Turtle()
emma.color("blue")
emma.pensize(0)

raf = turtle.Turtle()
raf.color("green")
raf.shape("turtle")
raf.pensize(3)
def square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)


def triangle(length):
    for i in range(3):
        emma.forward(length)
        emma.left(120)


'''print(list(range(60)))
raf.up()
raf.speed(2)
for size in range(200):

    raf.forward(2)
    raf.left(1)


raf.color("blue")'''
raf.up()
for size in range(10):
    raf.forward(90)
    raf.down()
    raf.forward(8)
    raf.up()
    raf.forward(15)
    raf.stamp()
    raf.forward(-113)
    raf.right(36)

#triangle(100)
#square(100)

turtle.done()
