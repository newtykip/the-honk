from string import ascii_lowercase as alphabet
from itertools import permutations

superscript = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

def factorial(n):
	ans = 1
	for i in range(2, n + 1):
		ans *= i
	return ans

def multinomialCoefficient(n, *k):
	ans = factorial(n)
	
	for i in k:
		ans //= factorial(i)

	return ans

while True:
	try:
		m = int(input('Please enter an amount of nomials to include (: '))

		if m > len(alphabet):
			raise ValueError

		selectedLetters = alphabet[:m]
		break
	except ValueError:
		print('Please ensure that you choose a valid amount of nomials (less than or equal to 26 please [:)')
		continue

while True:
	try:
		n = int(input('Please enter a power to put (%s) to! ' % ' + '.join(selectedLetters)))
		break
	except ValueError:
		print('The power must be a valid integer!')
		continue

# [{ letter: power }]
nomials = []
currentPower = {}

# Filter the power combinations for only where they add up to n
powerCombinations = list(set(permutations([i for i in range(0, n + 1)] * m, m)))

for combo in powerCombinations:
	if sum(combo) != n:
		continue

	powers = {}

	for i in range(len(combo)):
		letter = selectedLetters[i]
		powers[letter] = combo[i]

	nomials.append(powers)

formattedTerms = []

for nomial in nomials:
	coefficient = multinomialCoefficient(n, *nomial.values())
	term = ''

	if coefficient == 0:
		continue
	elif coefficient != 1:
		term += str(coefficient)

	for letter in nomial:
		power = nomial[letter]

		if power == 1:
			term += letter
		elif power > 0:
			powerString = ''

			for digit in str(power):
				powerString += superscript[int(digit)]

			term += '%s%s' % (letter, powerString)

	formattedTerms.append(term)

print(' + '.join(formattedTerms))

