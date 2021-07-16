#-------------------------------------------------------------------------------
# Name:        Temperature Bar Chart Project
# Purpose:     A turtle program that draws a bar chart based on an array of
#              inputted floats.
#-------------------------------------------------------------------------------

import turtle

# sub-routine to draw a bar
def drawBar(t, h):
    t.left(90)
    t.forward(h)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(h)
    t.left(90)

# collect data
inp = input('Please input your list of floats. Separate each float by a comma.')
inp = inp.split(',')

data = []
for i in inp:
    data.append(float(i))

maxheight = max(data)
numbars = len(data)
border = 10

# create a window
wn = turtle.Screen()
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor('lightgreen')

# create a turtle
t = turtle.Turtle()
t.color('blue')
t.fillcolor('red')
t.pensize(3)

# draw bars
for i in data:
    drawBar(t, i)

wn.exitonclick()
