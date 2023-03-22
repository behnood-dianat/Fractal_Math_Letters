import turtle
import math
import random
import numpy as np
# Create a Turtle object
t = turtle.Turtle()
turtle.tracer(0)
# Set the pen color to red and the dot size to 10
t.pencolor("red")
t.pensize(10)
vets=5 # Number of vetrices 
# Calculate the coordinates of the vertices of the pentagon
radius = 250  # The radius of the circle that circumscribes the pentagon
angle = 360 / vets  # The angle between each vertex of the pentagon
vertices = []
for i in range(vets):
    x = radius * math.cos(math.radians(i * angle - 90))
    y = radius * math.sin(math.radians(i * angle - 90))
    vertices.append((x, y))

# Draw the pentagon by moving to each vertex and drawing a dot
t.penup()
for vertex in vertices:
    t.goto(vertex)
    t.dot()
t.speed(0)

# Randomly select two vetrices

t.pencolor("black")
t.pensize(0.1)

a,b = random.sample(vertices,2)
for i in range(10000):
    x=np.average([a[0],b[0]])
    y=np.average([a[1],b[1]])
    t.goto([x,y])
    t.dot()
    n= [x for x in vertices if list(x) != b]
    b=random.sample(n,1)
    a=[x,y]
    b=[b[0][0],b[0][1]]

turtle.update()
# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
