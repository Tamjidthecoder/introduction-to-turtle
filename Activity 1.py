import turtle
turtle.Screen().bgcolor("Sky blue")
turtle.Screen().setup(300,500)
polygon=turtle.Turtle()
number_side=int(input("Enter a number: "))
side_len=92
angle=360/number_side
for i in range(number_side):
    polygon.forward(side_len)
    polygon.right(angle)

turtle.done()