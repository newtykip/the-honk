import math
from _helpers import listInput

def sd(x):
    n = len(x)
    mean = sum(x) / n
    squared = [y ** 2 for y in x]

    return math.sqrt(abs((sum(squared) / n) - (mean**2)))

nums = listInput('Please input a list of numbers')
res = sd(nums)

print()
print('The list:', nums)
print('Standard Deviation:', res)
