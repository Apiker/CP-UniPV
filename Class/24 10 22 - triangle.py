import turtle, math
ninja = turtle.Turtle() #create turtle (ninja)
ninja.speed(0) #determine turtle speed

a = 60
l = 200

x = 90 + a
b = 2 * l * math.sin(math.radians(a))

print(x)

ninja.left(a)
ninja.fd(l)
ninja.right(x)
ninja.fd(b)
ninja.right(x)
ninja.fd(l)


turtle.hideturtle()
turtle.mainloop()

