import operator

def diff(a):
	return list(map(operator.sub, a[1:], a[:-1]))

def formatNumber(x):
	if x % 1 == 0:
		return int(x)
	else:
		return x	

sequence = [-0.5,1,4.5,10,17.5]
row1 = diff(sequence)
row2 = diff(row1)

a = formatNumber(row2[0] / 2)
b = formatNumber(row1[0] - (3 * a))
c = formatNumber(sequence[0] - a - b)

print('''
a = {0}
b = {2}
c = {4}

Equation: {0}n²{1}{2}n{3}{4}
'''.format(a, '+' if b >= 0 else '', b, '+' if c >= 0 else '', c))
