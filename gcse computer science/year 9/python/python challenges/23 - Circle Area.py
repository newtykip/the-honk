import math

def turfRequired(l, w, r):
    garden = l * w
    circle = math.pi * (r ^ 2)

    return garden - circle

length = int(input('Please input the length of the lawn (in metres).'))
width = int(input('Please input the width of the lawn (in metres).'))
radius = int(input('Please input the radius of the circle (in metres).'))

print(turfRequired(length, width, radius))