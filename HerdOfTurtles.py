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

#background
A.speed(100)
A.color("white")
A.right(90)
A.forward(200)
A.color("black")
A.left(90)
A.color("yellow")
A.begin_fill()
A.circle(250)
A.end_fill()
#frame
A.color("black")
A.pensize(3)
A.circle(250)
A.color("white")
A.right(90)
A.forward(200)

#right eye
B.speed(100)
B.color("yellow")
B.left(90)
B.forward(150)
B.right(90)
B.forward(70)
B.color("Black")
B.pensize(30)
B.forward(40)

#left eye
C.speed(100)
C.color("yellow")
C.left(90)
C.forward(150)
C.right(90)
C.forward(-70)
C.color("Black")
C.pensize(30)
C.forward(-40)

#mouth
D.speed(100)
D.color("yellow")
D.right(90)
D.forward(80)
D.right(90)
D.forward(-70)
D.color("Black")
D.pensize(30)
D.forward(140)


turtle.exitonclick()