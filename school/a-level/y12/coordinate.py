from math import pi, cos, sin

n = 125
c = 6

r = n / 2
theta = 2 * pi / c

getCoordinate = lambda alpha: (r * (1 + cos(alpha)), r * (1 + sin(alpha)))
sectors = []

for i in range(c):
    print(i, getCoordinate(theta * i))