def karatsuba(x, y):
	xLen = len(str(x))
	yLen = len(str(y))
	# handle single digit multiplication at the end of the iteration
	# this gives the loop an end, and gives us our final results
	if xLen == 1 or yLen == 1:
		return x * y
	else:
		n = max(xLen, yLen) // 2 # choose the longest length
		# calculate a, b, c, d for the iteration
		a = x // (10 ** n)
		b = x % (10 ** n)
		c = y // (10 ** n)
		d = y % (10 ** n)
		# run karatsuba to resolve ac and bd for the iteration
		ac = karatsuba(a, c)
		bd = karatsuba(b, d)
		# use karatsuba again to resolve adbc for the iteration
		adbc = karatsuba(a + b, c + d) - ac - bd
		# return the solution for the digit pairs of the iteration
		return ac * 10 ** (2 * n) + (adbc * 10 ** n) + bd

# helper method to easily take in our inputs
def takeInput(text):
	while True:
		try:
			x = int(input(text))
			return x
		except ValueError:
			print('You must input an integer!\n')

num1 = takeInput('Please enter a number (:\n')
num2 = takeInput('Please enter a number to multiply it by!\n')

# Calculate the result and check if it is right
res = num1 * num2
karatsubaRes = karatsuba(num1, num2)

print()
print('Quadratic Result: ', res)
print('Karatsuba Result: ', karatsubaRes)

if res == karatsubaRes:
	print()
	print('The algorithm worked (:')
