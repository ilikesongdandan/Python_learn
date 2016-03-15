import turtle
def drawShape(sides,length):
	angle=360.0/sides
	for side in range(sides):
		turtle.forward(length)
		turtle.right(angle)

def movTurtle(x,y):
	# pass
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()

def drawSquare(length):
	drawShape(4, length)

def drawTriangle(length):
	drawShape(3, length)


def drawCircle(length):
	drawShape(360, length)
	# pass

drawShape(5, 20)
movTurtle(60, 30)
drawShape(3, 10)
movTurtle(-100,-100)
drawShape(3, -10)
movTurtle(100, 100)
drawSquare(20)
movTurtle(50, 50)
drawTriangle(30)
movTurtle(-50, -50)
drawCircle(2)


turtle.done()