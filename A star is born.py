import turtle


def star(size):
    for i in range(5):
        turtle.right(144)
        turtle.forward(size)

    return;


def spiral(x, y, size, number, angle):
    # move the turtle in x and y
    turtle.color("white")
    turtle.setx(x)
    turtle.sety(y)
    turtle.color("black")

    for i in range(number):
        star(size)
        size += 10
        turtle.right(angle)

    # align the turtle to the x axis
    turtle.right(360 - number * angle)

    return;


turtle.shape("turtle")
turtle.speed(1000)

spiral(-500, -500, 130, 50, 3)
spiral(0, 150, 130, 50, 3)
spiral(350, -500, 130, 50, 3)

turtle.exitonclick()