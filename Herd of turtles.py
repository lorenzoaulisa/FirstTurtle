import turtle

scn = turtle.Screen()
A = turtle.Turtle()
B = turtle.Turtle()
C = turtle.Turtle()
D = turtle.Turtle()

A.shape("turtle")
B.shape("turtle")
C.shape("turtle")
D.shape("turtle")

B.speed(1)
B.color("white")
B.left(90)
B.forward(150)
B.right(90)
B.forward(40)
B.color("Black")
B.pensize(30)
B.forward(30)

A.speed(1)
A.color("white")
A.right(90)
A.forward(200)
A.color("black")
A.left(90)
A.circle(250)


turtle.exitonclick()