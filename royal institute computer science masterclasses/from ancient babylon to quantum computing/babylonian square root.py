x = float(input('Please input the number to calculate the square root of! '))
a = 2

while abs((a - (x / a))) > 1:
	a = (a + (x / a)) / 2

print(a)
