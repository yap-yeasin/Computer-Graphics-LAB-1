import turtle
turtle.title("Draw Shahid Minar")

draw = turtle.Turtle()
draw.speed(10) 

draw.pensize(5)

draw.pu()
draw.goto(-300,-150) 
draw.pendown()
draw.pencolor("black")
draw.fd(600)

draw.left(180)
draw.fd(295)
draw.right(90)
draw.fd(295)
draw.left(180)
#left-1
draw.circle(-900,19)

draw.left(180)
draw.circle(900,19)
draw.left(180)
#left-2
draw.circle(-500,36)

draw.left(180)
draw.circle(500,36)
draw.left(180)
#left-3
draw.circle(-350,57)

draw.left(180)
draw.circle(350,57)
draw.left(180)
#left-4
draw.circle(-300,80)

draw.left(180)
draw.circle(300,80)
draw.left(180)

#Right-1
draw.circle(900,19)

draw.left(180)
draw.circle(-900,19)
draw.left(180)
#Right-2
draw.circle(500,36)

draw.left(180)
draw.circle(-500,36)
draw.left(180)
#Right-3
draw.circle(350,57)

draw.left(180)
draw.circle(-350,57)
draw.left(180)
#Right-4
draw.circle(300,80)

draw.left(180)
draw.circle(-300,80)
draw.left(180)

#Mid
draw.fd(200)
draw.left(180)
draw.left(35)

draw.fd(20)
draw.right(68)
draw.fd(20)

draw.left(210)

draw.left(35)
draw.fd(20)
draw.right(65)
draw.fd(20)


turtle.done()

