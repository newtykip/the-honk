from operator import not_

def getBit(prompt):
    while True:
        try:
            bit = int(input(prompt))

            if bit not in [0, 1]:
                raise ValueError('Please enter either a 1 or a 0')
            elif len(str(bit)) != 1:
                raise ValueError('Please make sure you only enter one bit')

            return bit
        except ValueError as err:
            if err.args[0].startswith('invalid'):
                print('Please make sure you input a valid integer')
            else:
                print(err)

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
        return ('^', lambda x, y: x & y)
    elif gate == 'OR':
        return ('∨', lambda x, y: x | y)
    elif gate == 'XOR':
        return ('⊕', lambda x, y: (x & not_(y)) | (not_(x) & y))
    elif gate == 'NAND':
        return ('↑', lambda x, y: not_(x & y))
    elif gate == 'NOR':
        return ('↓', lambda x, y: not_(x | y))
    elif gate == 'XNOR':
        return ('⊙', lambda x, y: (x & y) | (not_(x) & not_(y)))


A = getBit('Please enter bit A: ')
B = getBit('Please enter bit B: ')
symbol, applyGate = getGate()
Q = applyGate(A, B)

print(f'''Q = A {symbol} B
  = {A} {symbol} {B}
  = {Q}''')