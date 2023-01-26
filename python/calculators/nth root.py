from typing import Union
from _helpers import floatInput, intInput
from dataclasses import dataclass

@dataclass
class Result:
	result: Union[float, int]
	maxIterations: int
	iterationsUsed: int

superscript = [ '⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹' ]

def formatRadical(n: float, x: float):
	formattedN, formattedX = '', ''

	if int(n) == n:
		nString = str(int(n))

		for i in range(len(nString)):
			digit = int(nString[i])
			formattedN += superscript[digit]

	else:
		nString = str(n)

		for i in range(len(nString)):
			try:
				digit = int(nString[i])
				formattedN += superscript[digit]
			except:
				formattedN += '˙'

	if int(x) == x:
		formattedX = str(int(x))
	else:
		formattedX = str(x)
	
	return f"{formattedN}√{formattedX}"

def nthRoot(n: float, x: float, maxIterations: int = 200) -> Result:
	lastIteration, iteration, iterationsUsed = 0, 1, 0
	
	for _ in range(maxIterations):
		if lastIteration == iteration:
			break

		iterationsUsed += 1
		lastIteration = iteration
		iteration = ((iteration * (n - 1)) + (x * (iteration ** (1 - n)))) / n

	if int(iteration) == iteration:
		iteration = int(iteration)

	return Result(iteration, maxIterations, iterationsUsed)

print('ⁿ√x')
n = floatInput('Please input a value for n: ')
x = floatInput('Please input a value for x: ')
iterations = intInput('Please enter an amount of iterations to perform: ')
root = nthRoot(n, x, iterations)

print(f'\n{formatRadical(n, x)} = {root.result}')
print(f'Used {root.iterationsUsed} out of {root.maxIterations} iterations (:')
