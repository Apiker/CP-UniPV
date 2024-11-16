import turtle, math #importing libraries

pNumber = input("Inserisci numero petali: ")    #input: ask user how many petals the flower should have
pLenght = 300   #lenght of petals
pAngle = 40 #angle (width) of petals

ninja = turtle.Turtle() #create turtle (ninja)
ninja.speed(0) #determine turtle speed

def arc(ninja, pLenght, pAngle):  #arc function: draw and ark (half petal)
    step = (2 * math.pi * pLenght) / 360
    for i in range(pAngle):
        ninja.fd(step)
        ninja.lt(1)

def flower(ninja, pNumber, pLenght, pAngle):    #flower function: takes ark function and creates the shape
    for i in range(pNumber):    #loop the code for every petal
        for i in range(2):  #loop the code twice (each half petal >> 2 arches = 1 petal)
            arc(ninja, pLenght, pAngle) #call arc function
            ninja.lt(180 - pAngle)  #turn left 180 - 40 to create the second
        ninja.lt(360/pNumber)   #turn left 360/40 = 9 degrees to start another petal

flower(ninja, int(pNumber), pLenght, pAngle)    #call flower function

ninja.hideturtle()
turtle.mainloop()