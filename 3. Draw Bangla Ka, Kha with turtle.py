import turtle
turtle.title("Draw ka, kha")

draw = turtle.Turtle()
draw.speed(10) 

draw.pu()
draw.goto(-200,0) 
draw.pendown()

draw.pensize(10)
draw.pencolor("blue")

#ka
draw.left(45)
draw.fd(100)
draw.left(135)
draw.forward(75)
draw.left(180)
draw.fd(150)
draw.left(180)
draw.fd(75)
draw.left(90)
draw.fd(141)
draw.right(135)
draw.fd(100)
draw.right(145)

draw.pu()
draw.fd(70) 
draw.left(90)
draw.fd(30)
draw.right(30)
draw.pendown()
for i in range(15): 
	draw.right(15)  # rotation	 / Degree
	draw.forward(5) 	# radius/diameter

#positon changing for kha
draw.pu()
draw.left(180)
draw.fd(150)
draw.left(90)
draw.fd(65)
draw.pendown()

#kha
draw.circle(5)
draw.left(165)
draw.circle(25,180)
draw.left(180)
draw.circle(-80,60)
draw.left(135)
draw.fd(90)
# draw.pu()
# draw.pendown()
draw.right(-115)
draw.fd(115)
draw.right(90)
draw.fd(25)

turtle.done()

