import turtle


turtle.shape("turtle")
turtle.speed(4)

turtle.forward(10)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)


for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.forward(100)

def drawRec(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def drawRec(size, angle):
    for i in range(4):
        turtle.forward(size)
        turtle.right(360/angle)

drawRec(100)
drawRec(200)
drawRec(300)
