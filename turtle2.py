import turtle, random


t = turtle.Pen()


def my_circle(red, green, blue, radius):

    t.color(red, green, blue)
    for h in range(0,8):
        t.forward(radius)
        t.right(45)
    # t.begin_fill()
    # t.circle(radius)
    # t.end_fill()

for x in range(1,1000):
    my_circle(0,0 ,0, random.randint(1,100))
    t.up()
    t.right(random.randint(0,360))
    t.forward(random.randint(50,100))
    t.down()


turtle.done()


