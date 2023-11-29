from typing import Callable
from operator import and_, or_, xor

def applyOperator(binary: list, mask: list, operator: Callable[[int, int], list]) -> list:
    return [operator(a, b) for a, b in zip(binary, mask)]

def getBinary(prompt: str, length: int = None) -> list:
    while True:
        try:
            bits = list(input(f"{prompt} "))

            for bit in bits:
                if bit not in ["0", "1"]:
                    raise ValueError("Invalid binary number. Please try again.")
            
            if len(bits) == 0:
                raise ValueError("Please make sure you enter a value.")
            elif length and len(bits) != length:
                raise ValueError(f"Please make sure the value is {length} bits long.")

            return [int(x) for x in bits]
        except ValueError as error:
            print(error)

def makeChoice(prompt: str, choiceCount: int):
    while True:
        try:
            choice = int(input(f"{prompt} "))

            if choice < 1 or choice > choiceCount:
                raise ValueError("Please make a choice that is within bounds.")

            return choice
        except ValueError as error:
            print(error)

operators = {
    'AND':  ('&', lambda binary, mask: applyOperator(binary, mask, and_)),
    'OR': ('|', lambda binary, mask: applyOperator(binary, mask, or_)),
    'XOR': ('^', lambda binary, mask: applyOperator(binary, mask, xor))
}

# take in the binary values
binary = getBinary("Please enter your binary number:")
mask = getBinary("Please enter the mask:", len(binary))

# choose an operation
choices = [(i + 1, operator) for i, operator in enumerate(operators.keys())]

for i, operator in choices:
    print(f'{i}. {operator}')

symbol, operation = operators.get(choices[makeChoice("Please choose a logical operation:", len(choices)) - 1][1])
output = "".join(str(x) for x in operation(binary, mask))
binary, mask = "".join(str(x) for x in binary), "".join(str(x) for x in mask)

print(f"{binary} {symbol} {mask} = {output}")