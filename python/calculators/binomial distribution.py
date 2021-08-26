import operator as op
from functools import reduce
from _helpers import intInput, floatInput

def nCr(n, r):
    r = min(r, n-r)
    num = reduce(op.mul, range(n, n - r, -1), 1)
    den = reduce(op.mul, range(1, r + 1), 1)
    return num / den

def binomial(x, n, p):
    q = 1 - p
    return nCr(n, x) * (p ** x) * (q ** (n-x))

n = intInput('How many trials would you like to execute?')
x = intInput('How many times must the outcome happen in these trials?')
p = floatInput('What is the probability of success as a float?')
res = binomial(x, n, p)

print()
print(res)
