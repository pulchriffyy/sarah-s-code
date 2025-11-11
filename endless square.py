import turtle
a = turtle.Screen()
a.bgcolor("green")
p = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        p.forward(size+1)
        p.left(90)
        size = size - 5
    size = size + 1