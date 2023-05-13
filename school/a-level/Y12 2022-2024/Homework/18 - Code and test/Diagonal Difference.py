from typing import List, Callable
from random import randint
from functools import reduce
from operator import iconcat

def getInteger(prompt: str, err: str, validation: Callable[[int], bool] = None) -> int:
    """Fetch an integer from the user and validate it if necessary."""
    while True:
        try:
            value = int(input(prompt))
            
            if validation and validation(value):
                raise ValueError

            return value
        except ValueError:
            print(err)

def generateMatrix(n: int, min: int, max: int) -> List[List[int]]:
    """Generates an nxn square matrix and populates it with random integer values between two bounds."""
    if min > max:
        raise ValueError('Minimum value must be less than maximum value!')

    return [[randint(min, max) for _ in range(n)] for _ in range(n)]

def printMatrix(matrix: List[List[int]]):
    n = len(matrix)
    rowFormatting  = "{:^7}| "  * n
    divider = '-' * (n * 9 - 1)

    print(divider)

    for row in matrix:
        print(rowFormatting.format(*row))
        print(divider)

def diagonalSum(matrix: List[List[int]], left: bool = True) -> int:
    """Computes the diagonal sum of an nxn square matrix."""
    sum = 0
    n = len(matrix)

    for i, row in enumerate(matrix):
        if left:
            sum += row[i]
        else:
            sum += row[n - i - 1]

    return sum 

def diagonalDifference(matrix: List[List[int]]) -> int:
    """Computes the diagonal difference of an nxn square matrix."""
    left = diagonalSum(matrix)
    right = diagonalSum(matrix, False)
    
    return abs(right - left)

def sumOfCorners(matrix: List[List[int]]) -> int:
    """Computes the sum of the corners of an nxn square matrix."""
    n = len(matrix)

    return matrix[0][0] + matrix[0][n - 1] + matrix[n - 1][0] + matrix[n - 1][n - 1]

def averageValue(matrix: List[List[int]]) -> int:
    """Computes the average value in an nxn square matrix."""
    values = reduce(iconcat, matrix, [])

    return sum(values) / (len(matrix) ** 2)

n = getInteger('Please enter the dimension of the square matrix: ', 'Please enter a natural number greater than 1.', lambda x: x <= 1)
matrix = generateMatrix(n, 1, 100)
# matrix = [[12,3,15],[4,7,8],[5,6,2]]
difference = diagonalDifference(matrix)
corners = sumOfCorners(matrix)
average = averageValue(matrix)

printMatrix(matrix)
print(f"""Diagonal difference: {difference}
Sum of the corners: {corners}
Average value: {average}""")
