from string import ascii_uppercase
from functools import reduce

def bold(string):
    return f' \033[1m{string}\033[0m '

def red(string):
    return f' \033[91m{string}\033[0m '

def NOT(x):
    return 0 if x == 1 else 1 

def AND(x, y):
    return x & y

def OR(x, y):
    return x | y

def XOR(x, y):
    return OR(AND(x, NOT(y)), AND(NOT(x), y))

def NAND(x, y):
    return NOT(AND(x, y))

def NOR(x, y):
    return NOT(OR(x, y))

def XNOR(x, y):
    return OR(AND(x, y), NOR(x, y))

ALPHABET = list(map(lambda x: bold(x), ascii_uppercase))[0:20]

def getGate():
    while True:
        try:
            gate = input('Please enter a gate to apply: ').upper()

            if gate not in ['AND', 'OR', 'XOR', 'NAND', 'NOR', 'XNOR']:
                raise ValueError

            break
        except ValueError:
            print('Please enter a valid gate. Possible choices: AND, OR, XOR, NAND, NOR, XNOR')

    if gate == 'AND':
        return '^', lambda *values: reduce(AND, values)
    elif gate == 'OR':
        return '∨', lambda *values: reduce(OR, values)
    elif gate == 'XOR':
        return '⊕', lambda *values: reduce(XOR, values)
    elif gate == 'NAND':
        return '↑', lambda *values: reduce(NAND, values)
    elif gate == 'NOR':
        return '↓', lambda *values: reduce(NOR, values)
    elif gate == 'XNOR':
        return '⊙', lambda *values: reduce(XNOR, values)

def getInputs():
    while True:
        try:
            # Anything past 20 takes too long to compute the Cartesian product for
            amount = int(input('How many inputs would you like (2-20): '))

            if amount < 2 or amount > 20:
                raise ValueError
            
            break
        except ValueError:
            print('Please enter a valid integer between 2 and 20 inclusive.')

    formatString = ' {: ^3} |' + (' {: ^3} |' * amount) + ' {: ^3}'
    
    return amount, formatString

inputQuantity, formatString = getInputs()
gate, applyGate = getGate()
header = formatString.format(bold('#'), *ALPHABET[0:inputQuantity], bold(gate))

print(header)
print('-' * (len(header) - 15 - (8 * inputQuantity)))

# Find the cartesian product to generate pairs
# https://en.wikipedia.org/wiki/Cartesian_product
sets = [(0, 1)] * inputQuantity
print(sets)
pairs = [[]]

for set in sets:
    pairs = [x+[y] for x in pairs for y in set]

print(pairs)

for i, pair in enumerate(pairs):
    print(formatString.format(red(i + 1), *pair, bold(applyGate(*pair))))