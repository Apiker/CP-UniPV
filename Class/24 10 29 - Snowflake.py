import turtle

def koch(t, n):
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    for i in range(3):
        koch(t, n)
        t.rt(120)

n = int(input("n value:  "))

ninja = turtle.Turtle()
ninja.speed(0)

ninja.pu()
ninja.goto(-150, 90)
ninja.pd()
snowflake(ninja, n)


turtle.done()