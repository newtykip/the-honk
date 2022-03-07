def nthRoot(n: int, x: int):
	lastX = None
	y = 1 # initial guess

	while y != lastX:
		# f(y) = yⁿ - x
		# f'(y) = nyⁿ⁻¹
		f = (y ** n) - x
		fprime = n * (y ** (n - 1))
		
		lastX = y
		y -= f / fprime

	return y

print(nthRoot(5, 6 ** 6))
