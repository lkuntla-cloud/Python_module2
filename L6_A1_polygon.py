import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
sides=6
sidelen=70
angle=360/sides

for i in range (sides):
    polygon.forward(sidelen)
    polygon.right(angle)

turtle.done()