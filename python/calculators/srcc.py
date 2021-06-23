import numpy

def rank(x):
    y = x.sort()
    print(y)
    res = []
    for i in x:
        res.append(y.index(x[i]) + 1)
    return res

def spearman(a, b):
    if len(a) != len(b):
        print('Both datasets must be the same length!')
        return undefined

    n = len(a)

    # rank set a
    aranks = sorted(range(n), reverse=True, key=a.__getitem__)
    print(aranks)

    # rank set b
    branks = rank(b)

    # work out the difference between ranks
    d = aranks - branks
    d = d**2
    d = numpy.sum(d)

    # plug the values into the formula
    return 1 - ((6*d) / (n**3 - n))

print(spearman([1,2,3,5,4], [5,4,3,2,1]))