"""
A square root calculator based on the Babylonian's approach!
Created as a part of my Royal Institute masterclass
"""

from _helpers import intInput

def sqrt(number):
	initialGuess = 2
	while abs(initialGuess - (number / initialGuess)) > 1:
		initialGuess = (initialGuess + (number / initialGuess)) / 2
	return int(initialGuess)

num = intInput('Please input a number! (:')
res = sqrt(num)

print()
print('Square Root:', res)
