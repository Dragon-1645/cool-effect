import turtle

t = turtle.Turtle()

t.speed(0)

turtle.bgcolor("black")

for i in range(240):
    t.color("cyan")
    t.circle(i)
    t.right(5)

turtle.done()