from operator import mul
import math
from _helpers import listInput

def pmcc(x, y):
    if len(x) != len(y):
        raise Exception('Both datasets must be the same length!')

    n = len(x)
    xy = list(map(mul, x, y))
    xsq = [z**2 for z in x]
    ysq = [z**2 for z in y]

    sxy = sum(xy) - ((sum(x) * sum(y)) / n)
    sxx = sum(xsq) - ((sum(x)**2) / n)
    syy = sum(ysq) - ((sum(y)**2) / n)

    return sxy / math.sqrt(sxx * syy)

a = listInput('Please input a list of numbers')
b = listInput('Please input a second list of numbers')
res = pmcc(a, b)

print()
print('List A:', a)
print('List B:', b)
print('PMCC:', res)
