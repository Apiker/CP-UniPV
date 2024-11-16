# flower_sol.py

import turtle
import math
import polyline

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

        
def circle(t, r):
    arc(t, r, 360)

def petal(t, length, angle):
    """
    Draw a petal
        t: Turtle
        length: petal length (in pixels)
        angle: petal angle (in degrees)
                angle between the tangents
                at the same vertex
    Preconditions: t is at one of the vertices
        and heading to the other vertex
    Postconditions: t position and direction
        are as at the beginning of the function
        (and the petal has been drawn)
    """
    
    angle_rad = angle/180*math.pi
    radius = length / (2 * math.sin(angle_rad/2))
    t.rt(angle/2) # head for the first side
    arc(t, radius, angle) # draw the first side
    t.lt(180-angle) # turn for the second side
    arc(t, radius, angle) # draw the second side
    t.lt(180-angle/2) # return to the initial direction

def flower(t, n, length, angle):
    """
    Draw a flower
        n: number of petals
        length: petal length
        angle: petal angle 
    """

    for i in range(n):
        petal(t, length, angle)
        t.lt(360/n)
        
########## MAIN ###########

bob = turtle.Turtle()
bob.speed(0)
#bob.fd(100)
#petal(bob, 200, 30)
n = 10
flower(bob, n, 100, 360/n)
#bob.fd(100)
