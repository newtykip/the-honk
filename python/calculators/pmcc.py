from operator import mul
import math

def pmcc(x, y):
    if len(x) != len(y):
        raise Exception('List x must be of the same length as list y. List x is {0} values long, whereas list y is {1} values long.'.format(len(x), len(y)))

    n = len(x)
    xy = list(map(mul, x, y))
    xsq = [z**2 for z in x]
    ysq = [z**2 for z in y]

    sxy = sum(xy) - ((sum(x) * sum(y)) / n)
    sxx = sum(xsq) - ((sum(x)**2) / n)
    syy = sum(ysq) - ((sum(y)**2) / n)

    return sxy / math.sqrt(sxx * syy)

print(pmcc([1,2,3,4,5], [5,3,8,7,12]))