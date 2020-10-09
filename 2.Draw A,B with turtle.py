import turtle
turtle.title("Draw A, B")

# Circle Part
draw = turtle.Turtle()
# draw.speed(10)

draw.pu()
draw.goto(-200,0) # .goto(x, y)
draw.pendown()

# draw.shape("circle")
draw.pensize(10)
draw.pencolor("blue")

#A
draw.left(60)
draw.forward(200)
draw.right(120)
draw.forward(100)

draw.right(120)
draw.forward(95)
draw.right(180)

draw.forward(95)
draw.right(60)
draw.forward(100)

#B
draw.pu()
draw.left(60)
draw.forward(100)
draw.left(90)
draw.pendown()
draw.forward(180)
draw.right(90)

draw.circle(-45,180) #.circle(radius, extent=None, steps=None) minus diye direction change korchi
draw.right(180)
draw.circle(-45,180)

# B by for loop
draw.pu()
draw.left(180)
draw.forward(150)
draw.left(90)
draw.pendown()
draw.forward(180)
draw.right(90)

x=11
y=15
z=12
#half circle
for i in range(x): 
	draw.right(y)  # rotation	 / Degree
	draw.forward(z) 	# radius/diameter
draw.right(180)
#half circle
for i in range(12): 
	draw.right(16)  # rotation	 / Degree
	draw.forward(12) 	# radius/diameter

turtle.done()
# turtle.Screen().exitonclick()
