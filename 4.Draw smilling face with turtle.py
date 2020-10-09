import turtle 
turtle.title("Draw smiling face")

pen = turtle.Turtle() 

def eye(col, rad): 
	pen.down() 
	pen.fillcolor(col) 
	pen.begin_fill() 
	pen.circle(rad) 
	pen.end_fill() 
	pen.up() 

#graph line with X-axix , Y-axix
# X-axix
pen.fd(500)
pen.left(180)
pen.fd(1000)
pen.left(180)
pen.fd(500)
# Y-axix
pen.left(90)
pen.fd(500)
pen.left(180)
pen.fd(1000)
pen.left(180)
pen.fd(500)
pen.right(90)

# draw face 
pen.fillcolor('yellow') 
pen.begin_fill() 
pen.circle(100) 
pen.end_fill() # fillcolor off
pen.up() 

# draw mouth 
pen.width(4) 
pen.goto(-50, 60) 
pen.down() 
pen.right(45) 
pen.circle(70, 90) 
pen.up() 

# draw eyes 
pen.width(2) 
pen.goto(-30, 120) 
eye('white', 15) 
pen.goto(-37, 125) 
eye('black', 5) 
pen.goto(50, 120) 
eye('white', 15) 
pen.goto(43, 125) 
eye('black', 5) 
pen.up()
pen.goto(4000, 1250) 
turtle.done()