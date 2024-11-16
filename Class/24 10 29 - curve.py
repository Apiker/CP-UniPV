import turtle

def draw(t, lenght, n):
    if n == 0:
        return
    angle = 50
    t.fd(lenght*n)
    t.lt(angle)
    draw(t, lenght, n-1)
    t.rt(2*angle)
    draw(t, lenght, n-1)
    t.lt(angle)
    t.bk(lenght*n)

lenght = int(input("lenght: "))
n = int(input("n value: "))

ninja = turtle.Turtle()



draw(ninja, lenght, n)

turtle.done()
