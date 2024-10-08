import turtle

t = turtle.Turtle()


def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def spirala():
    t.reset()
    for i in range(100):
        t.forward(i)
        t.left(50)


def kruh():
    t.reset()
    for i in range (120):
        t.forward(3)
        t.left(3)

def ctverec():
    t.reset()
    for i in range(4):
        t.forward(100)
        t.left(90)

def srdce():
    t.reset()
    t.fillcolor('red')

    t.begin_fill()

    t.left(140)
    t.forward(113)

    curve()
    t.left(120)

    curve()

    t.forward(112)

    t.end_fill()