import turtle

turtle.shape("turtle")


def Italy():
    for i in range(3):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(250)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(250)
        turtle.right(90)
        turtle.forward(100)
        turtle.forward(200)

Italy()

turtle.exitonclick()