import turtle
# from turtle import Screen
turtle.title("Circle, Line, Rectangle")

# screen = Screen()
# TURTLE_SIZE = 5

# Circle Part
draw = turtle.Turtle()
draw.speed(1)

draw.pu()
# draw.goto(TURTLE_SIZE/2 - screen.window_width()/4, screen.window_height()/6 - TURTLE_SIZE/2)
draw.goto(-200,0) # .goto(x, y)
draw.pendown()

draw.shape("circle")
draw.pensize(10)
draw.pencolor("blue")
# draw.fillcolor("orange")

draw.circle(100) # Diameter


# Line
draw.penup() #draw.pu()
draw.forward(150)
draw.left(90)
draw.forward(100)
draw.right(90)
draw.pendown()
draw.forward(150)

# Rectangle
draw.penup() #draw.pu()
draw.forward(50)
draw.left(90)
draw.forward(50)
draw.right(90)
draw.pendown()
draw.forward(200)
draw.right(90)
draw.forward(100)
draw.right(90)
draw.forward(200)
draw.right(90)
draw.forward(100)


turtle.done()
# turtle.Screen().exitonclick()
