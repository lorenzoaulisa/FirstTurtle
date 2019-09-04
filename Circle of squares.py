import turtle

turtle.shape("turtle")
turtle.speed(20)

for i in range(60):
    for j in range(4):
        turtle.forward(150)
        turtle.right(90)

    turtle.right(5)

turtle.exitonclick()