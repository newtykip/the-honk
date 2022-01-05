from math import e
from _helpers import floatInput

def sin(radians):
	x = radians
	return (((e ** (1j * x)) - (e ** -(1j * x))) / 2j).real

def cos(radians):
	x = radians
	return (((e ** (1j * x)) + (e ** -(1j * x))) / 2).real

def tan(radians):
	x = radians
	return (((e ** (1j * x)) - (e ** -(1j * x))) / (1j * ((e ** (1j * x)) + (e ** -(1j * x))))).real

a = floatInput("Please enter an amount of radians: ")

print("""Where x = %i:
sin(x) = %f
cos(x) = %f
tan(x) = %f
""" % (a, sin(a), cos(a), tan(a)))
