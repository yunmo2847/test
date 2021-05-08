import turtle,random

t = turtle.Turtle()
t.pensize(3)

for i in range(20):
    r = random.random()
    g = random.random()
    b = random.random()

    x = random.randint(-300,300)
    y = random.randint(-300,300)
    length = random.randint(10,300)

    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(r,g,b)
    t.begin_fill()
    for j in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()
    
