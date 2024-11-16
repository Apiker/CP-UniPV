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

n = int(input("n value: "))

ninja = turtle.Turtle()
ninja.speed(0)

koch(ninja, n)


turtle.done()