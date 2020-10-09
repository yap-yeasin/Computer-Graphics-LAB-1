import turtle 
turtle.title("Draw smiling face")

pen = turtle.Turtle() 
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

#Flag
pen.fillcolor('green') 
pen.begin_fill() 
pen.up()
pen.goto(200,100)
pen.down()
pen.right(90)
pen.fd(200)
pen.right(90)
pen.fd(400)
pen.right(90)
pen.fd(200)
pen.right(90)
pen.fd(400)
pen.end_fill() # fillcolor off
pen.up()
#Flag
pen.goto(0,-50)
pen.down()
pen.fillcolor('red') 
pen.begin_fill() 
pen.circle(50)
pen.end_fill() # fillcolor off
pen.up() 
pen.goto(1000,1000)

turtle.done()