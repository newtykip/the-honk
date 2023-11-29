from __future__ import annotations
from random import uniform
from typing import List, Iterable, Callable, Union
from functools import reduce
from operator import iconcat

class OperationError(Exception):
    pass

class MatrixRow:
    def __init__(self, length: int):
        self.__values: List[float] = [0 for _ in range(length)]
        self.__length = length

    def __getitem__(self, column: int):
        """Index the row."""
        if column <= 0 or column > self.__length:
            raise IndexError("Out of bounds")
        
        return self.__values[column - 1]

    def __setitem__(self, column: int, newValue: float):
        """Update a value in the row at a given column."""
        if column <= 0 or column > self.__length:
            raise IndexError("Out of bounds")

        self.__values[column - 1] = newValue

    def __iter__(self) -> Iterable:
        processedValues = []

        for value in self.__values:
            if type(value) == float and value.is_integer():
                processedValues.append(int(value))
            else:
                processedValues.append(value)

        return iter(processedValues)


class SquareMatrix:
    def __init__(self, n: int):
        self.__rows: List[MatrixRow] = [MatrixRow(n) for _ in range(n)]
        self.__n = n
        self.__rowFormatting = "{:^10}| " * n
        self.__divider = "-" * (n * 12)

    @staticmethod
    def From(rows: List[List[float]]) -> SquareMatrix:
        n = len(rows)

        if len(set([len(row) for row in rows])) != 1 or len(rows[0]) != n:
            raise ValueError("Rows do not form a valid square matrix.")

        matrix = SquareMatrix(n)

        for i in range(n):
            for j in range(n):
                matrix[i + 1][j + 1] = rows[i][j]
        
        return matrix

    def size(self) -> int:
        """Returns the size of the square matrix."""
        return self.__n

    def populate(self, minimum: float, maximum: float) -> SquareMatrix:
        """Populates the matrix with random values."""
        if minimum > maximum:
            raise ValueError('Minimum value must be less than maximum value!')

        for i in range(1, self.__n + 1):
            for j in range(1, self.__n + 1):
                self[i][j] = uniform(minimum, maximum)

        return self

    def sumCorners(self) -> float:
        """Computes the sum of the corners of the matrix."""
        return self[1][1] + self[1][self.__n] + self[self.__n][1] + self[self.__n][self.__n]

    def values(self) -> float:
        """Return a list of all of the values in a matrix."""
        return reduce(iconcat, self.__rows, [])

    def averageValue(self) -> float:
        """Computes the avaerage value in the matrix."""
        return sum(self.values()) / (self.__n ** 2)

    def diagonalSum(self, left: bool = True) -> float:
        """Computes a diagonal sum of the matrix."""
        sum = 0
        
        for i, row in enumerate(self.__rows):
            if left:
                sum += row[i + 1]
            else:
                sum += row[self.__n - i]

        return sum

    def diagonalDifference(self) -> float:
        """Computes the diagonal difference of the matrix."""
        left = self.diagonalSum()
        right = self.diagonalSum(False)

        return abs(right - left)

    def transpose(self) -> SquareMatrix:
        """Transpose the matrix."""
        transposed = list(zip(*self.__rows))

        for i in range(self.__n):
            for j in range(self.__n):
                self[i + 1][j + 1] = transposed[i][j]

        return self

    def __str__(self) -> str:
        """Represents the matrix in a string."""
        out = self.__divider
        
        for row in self.__rows:
            out += f"\n|{self.__rowFormatting.format(*row)}\n{self.__divider}"

        return out

    def __getitem__(self, row: int):
        """Allows indexing of the matrix"""
        if row - 1 > self.__n:
            raise IndexError("Out of bounds")

        return self.__rows[row - 1]

    def __applyToMatrices(self, matrix: SquareMatrix, method: Callable[[float, float], float]) -> SquareMatrix:
        """Returns a new matrix containing the results of a method applied to the corresponding values of this matrix, and another one."""
        if matrix.size() != self.__n:
            raise OperationError("Matrix sizes are incompatible")

        newMatrix = SquareMatrix(self.__n)

        for i in range(1, self.__n + 1):
            for j in range(1, self.__n + 1):
                newMatrix[i][j] = method(self[i][j], matrix[i][j])

        return newMatrix

    def __applyToSelf(self, method: Callable[[float], float]) -> SquareMatrix:
        """Returns a new matrix containing the results of a method applies to the value of this matrix."""
        newMatrix = SquareMatrix(self.__n)

        for i in range(1, self.__n + 1):
            for j in range(1, self.__n + 1):
                newMatrix[i][j] = method(self[i][j])

        return newMatrix

    def __add__(self, value: Union[SquareMatrix, float]) -> SquareMatrix:
        """Add two matrices."""
        if isinstance(value, SquareMatrix):
            return self.__applyToMatrices(value, lambda x, y: x + y)
        else:
            return self.__applyToSelf(lambda x: x + value)

    def __sub__(self, value: Union[SquareMatrix, float]) -> SquareMatrix:
        """Subtract two matrices."""
        if isinstance(value, SquareMatrix):
            return self.__applyToMatrices(value, lambda x, y: x - y)
        else:
            return self.__applyToSelf(lambda x: x - value)

    def __mul__(self, scalar: float) -> SquareMatrix:
        """Multiply the matrix by a scalar."""
        return self.__applyToSelf(lambda x: x * scalar)

    def __floordiv__(self, scalar: float) -> SquareMatrix:
        """Floor divide the matrix by a scalar."""
        return self.__applyToSelf(lambda x: x // scalar)

    def __mod__(self, scalar: float) -> SquareMatrix:
        """Modulo the matrix by a scalar."""
        return self.__applyToSelf(lambda x: x % scalar)

    def __pow__(self, scalar: float) -> SquareMatrix:
        """Power the matrix by a scalar."""
        return self.__applyToSelf(lambda x: x ** scalar)

a = SquareMatrix.From([[12.4,3,15],[4,7,8],[5,6,2]])

print(a)
