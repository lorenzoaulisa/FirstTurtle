import turtle


def patch1():
    for i in range(40):
        turtle.right(90)
        turtle.forward(84)
        turtle.left(90)
        turtle.forward(1)
        turtle.left(90)
        turtle.forward(84)
        turtle.right(90)

    return;


def patch2():
    for i in range(14):
        turtle.forward(120)
        turtle.right(90)
        turtle.forward(1)
        turtle.right(90)
        turtle.forward(120)
        turtle.left(90)
        turtle.forward(1)
        turtle.left(90)

    return;


def frame():
    for i in range(2):
        turtle.right(90)
        turtle.forward(84)
        turtle.right(90)
        turtle.forward(120)
    return;


def Italy():
    turtle.color("green")
    patch1()
    turtle.color("white")
    patch1()
    turtle.color("red")
    patch1()
    turtle.color("black")
    frame()
    turtle.color("white")
    return;


def Romania():
    turtle.color("blue")
    patch1()
    turtle.color("yellow")
    patch1()
    turtle.color("red")
    patch1()
    turtle.color("black")
    frame()
    turtle.color("white")
    return;


def France():
    turtle.color("blue")
    patch1()
    turtle.color("white")
    patch1()
    turtle.color("red")
    patch1()
    turtle.color("black")
    frame()
    turtle.color("white")
    return;


def Russia():
    turtle.color("white")
    patch2()
    turtle.color("blue")
    patch2()
    turtle.color("red")
    patch2()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(84)
    turtle.right(90)
    turtle.color("black")
    frame()
    turtle.color("white")
    return;


turtle.speed(1000)

turtle.color("white")

turtle.forward(-400)

Italy()

turtle.forward(80)

Romania()

turtle.forward(80)

France()

turtle.forward(80)

Russia()

turtle.forward(80)

turtle.exitonclick()