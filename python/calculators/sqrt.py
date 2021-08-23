def sqrt(x):
	a = 2
	while abs((a - (x / a))) > 1:
		a = (a + (x / a)) / 2
	return int(a)

print(sqrt(81))
