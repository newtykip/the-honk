from _helpers import intInput

def karatsuba(x, y):
	xLen = len(str(x))
	yLen = len(str(y))
	# fallback to traditional multiplication
	if xLen == 1 or yLen == 1:
		return x * y
	else:
		n = max(xLen, yLen) // 2 # choose the largest size
		# split the digit sequences in the middle using some mathematical magic
		low1 = x % (10 ** n)
		low2 = y % (10 ** n)
		high1 = x // (10 ** n)
		high2 = y // (10 ** n)
		# 3 recursive calls made to numbers approximately half the size
		z0 = karatsuba(low1, low2)
		z1 = karatsuba(low1 + high1, low2 + high2)
		z2 = karatsuba(high1, high2)
		# plug it into the formula
		return (z2 * 10 ** (n * 2)) + ((z1 - z2 - z0) * (10 ** n)) + z0

num1 = intInput('Please enter a number (:')
num2 = intInput('Please enter a number to multiply it by!')

# Calculate the result and check if it is right
res = num1 * num2
karatsubaRes = karatsuba(num1, num2)

print()
print('Quadratic Result:', res)
print('Karatsuba Result:', karatsubaRes)

if res == karatsubaRes:
	print()
	print('The algorithm worked (:')
