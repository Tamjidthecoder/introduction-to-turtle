import turtle
turtle.Screen().bgcolor("blue")
turtle.title("turtle")
spiral=turtle.Turtle
size=0
while True:
    for i in range(4):
        spiral.fd(size + 1)
        spiral.left(90)
        size=size -5
    size=size+ 1
    turtle.done()    