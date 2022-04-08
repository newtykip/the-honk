import math

pi = 0

for k in range(20):
	numerator = (2 ** k) * (math.factorial(k) ** 2)
	denominator = math.factorial((2 * k) + 1)

	pi += numerator / denominator

pi *= 2
print(pi)
