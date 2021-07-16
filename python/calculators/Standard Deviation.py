import math

def sd(x):
    n = len(x)
    mean = sum(x) / n
    squared = [y ** 2 for y in x]

    return math.sqrt(abs((sum(squared) / n) - (mean**2)))

print(sd([135,230,132,323]))