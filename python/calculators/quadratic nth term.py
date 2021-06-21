import operator

def diff(a):
	return list(map(operator.sub, a[1:], a[:-1]))

sequence = [-0.5,1,4.5,10,17.5]
row1 = diff(sequence)
row2 = diff(row1)

a = row2[0] / 2
b = row1[0] - (3 * a)
c = sequence[0] - a - b

print('''
a = {0}
b = {1}
c = {2}

Equation: {0}n^2 + {1}n + {2}
'''.format(a, b, c))
