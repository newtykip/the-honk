import operator as op
from functools import reduce

def nCr(n, r):
    r = min(r, n-r)
    num = reduce(op.mul, range(n, n - r, -1), 1)
    den = reduce(op.mul, range(1, r + 1), 1)
    return num / den

def binomial(x, n, p):
    q = 1 - p
    return nCr(n, x) * (p**x) * (q**(n-x))

print(binomial(5, 100, 0.1))
