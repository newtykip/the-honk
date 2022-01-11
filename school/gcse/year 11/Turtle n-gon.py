from turtle import Turtle, Screen, numinput, textinput
from random import random

def generateColour():
    return (random(), random(), random())

# Configure the turtle
turtle = Turtle()

while True:
    # Change the colour of the turtle
    r, g, b = generateColour()
    turtle.color(r, g, b)

    # Collect the amount of sides
    while True:
        try:
            sides = int(numinput('Side Count', 'How many sides would you like to render?'))

            if sides < 3:
                raise ValueError
            else:
                break
        except ValueError:
            print('A polygon must have a minimum of 3 sides! Try again with a number >= 3')
            continue

    # Move the turtle
    for i in range(sides):
        turtle.forward(100)
        turtle.left(360 / sides)

    # Ask if the user would like to go again
    while True:
        try:
            again = textinput('Continue?', 'Would you like to run the program again?').lower()

            if not again == 'yes' and not again == 'no' and not again == 'y' and not again == 'n':
                raise ValueError
            else:
                break
        except ValueError:
            print('You must answer yes or no to this question')
            continue

    if again == 'y' or again == 'yes':
        # Reset the turtle and ask again
        turtle.reset()
    else:
        # Close the turtle
        Screen().bye()
        break