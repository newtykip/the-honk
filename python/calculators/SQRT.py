"""
A square root calculator based on the Babylonian's approach!
Created as a part of my Royal Institute masterclass
"""

from _helpers import intInput

def sqrt(x):
	a = 2
	while abs((a - (x / a))) > 1:
		a = (a + (x / a)) / 2
	return int(a)

num = intInput('Please input a number! (:')
res = sqrt(num)

print()
print('Square Root:', res)
