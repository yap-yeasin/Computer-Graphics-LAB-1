import turtle
turtle.title("Draw Shahid Minar")

draw = turtle.Turtle()
draw.speed(10) 

# draw.pu()
# draw.goto(-200,0) 
# draw.pendown()

draw.pensize(10)
draw.pencolor("red")
# Mid Circle
draw.fillcolor("red")
draw.begin_fill()
draw.circle(55)
draw.end_fill()

draw.pu()
draw.goto(-250,-150) 
draw.pendown()
draw.pencolor("black")
draw.fd(500)
#right 1
draw.left(90)
draw.fd(200)
draw.left(90)
draw.fd(50)
draw.left(90)
draw.fd(200)
#right 2
draw.right(90)
draw.fd(50)
draw.right(90)
draw.fd(250)
draw.left(90)
draw.fd(50)
draw.left(90)
draw.fd(250)
#mid
draw.right(90)
draw.fd(50)

draw.right(90)
draw.fd(300)
draw.right(10)
draw.fd(40)
draw.left(90)
draw.fd(50)
draw.left(90)
draw.fd(40)
draw.left(10)
draw.fd(308)

draw.right(180)
draw.fd(300)
draw.right(10)
draw.fd(48)
draw.left(90)
draw.fd(50)
draw.left(90)
draw.fd(48)
draw.left(10)
draw.fd(308)
#left 2
draw.right(90)
draw.fd(50)
draw.right(90)
draw.fd(250)
draw.left(90)
draw.fd(50)
draw.left(90)
draw.fd(250)

#left 1
draw.right(90)
draw.fd(50)
draw.right(90)
draw.fd(200)
draw.left(90)
draw.fd(50)
draw.left(90)
draw.fd(200)


turtle.done()

