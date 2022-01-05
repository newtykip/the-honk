import numpy
from _helpers import listInput

def rank(x):
    x = numpy.array(x)
    return x.argsort().argsort()

def spearman(a, b):
    if len(a) != len(b):
        raise Exception('Both datasets must be the same length!')

    n = len(a)

    # calculate rankings
    aranks = rank(a)
    branks = rank(b)

    # work out the difference between ranks
    d = aranks - branks
    d = numpy.sum(d ** 2)

    # plug the values into the formula
    return 1 - ((6 * d) / (n ** 3 - n))

a = listInput('Please input a list of numbers')
b = listInput('Please input a second list of numbers')
res = spearman(a, b)

print()
print('List A:', a)
print('List B:', b)
print('SRCC:', res)
