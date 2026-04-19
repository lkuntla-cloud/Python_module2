import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(400,400)
square=turtle.Turtle()
sides=4
sidelen=100
angle=360/sides

for i in range (sides):
    square.forward(sidelen)
    square.right(angle)

turtle.done()