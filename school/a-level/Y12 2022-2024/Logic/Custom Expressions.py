from enum import Enum
from typing import Tuple, List

class Gate(Enum):
    AND = '^'
    OR = '∨'
    XOR = '⊕'
    NAND = '↑'
    NOR = '↓'
    XNOR = '⊙'

class Symbol:
    def __init__(self, character):
        self.char = character

    def __str__(self):
        return self.char

class Expression:
    def __init__(self, symbol):
        self.tree: List[Tuple[Gate, Expression]] = []
        self.initialSymbol = symbol

    def AND(self, symbol):
        self.tree.append((Gate.AND, symbol))
        return self

    def OR(self, symbol):
        self.tree.append((Gate.OR, symbol))
        return self

    def XOR(self, symbol):
        self.tree.append((Gate.XOR, symbol))
        return self

    def NAND(self, symbol):
        self.tree.append((Gate.NAND, symbol))
        return self

    def NOR(self, symbol):
        self.tree.append((Gate.NOR, symbol))
        return self

    def XNOR(self, symbol):
        self.tree.append((Gate.XNOR, symbol))
        return self

    @staticmethod
    def treeSymbols(tree):
        symbols = set([])

        for _, value in tree:
            if isinstance(value, Expression):
                if str(value.initialSymbol) not in symbols:
                    symbols.add(str(value.initialSymbol))
                symbols.update(Expression.treeSymbols(value.tree))
            elif str(value) not in symbols:
                symbols.add(str(value))

        return symbols


    def compile(self):
        # Count symbols
        symbols = Expression.treeSymbols(self.tree)

        def run(*values):
            for gate, value in self._tree:

    def __str__(self):
        out = str(self.initialSymbol)

        for gate, value in self.tree:
            if isinstance(value, Expression) and len(value.tree) > 0:
                expression = f'({value})'
            else:
                expression = str(value)

            out += f' {gate.value} {expression}'

        return out
    
A = Symbol('A')
B = Symbol('B')
C = Symbol('C')
D = Symbol('D')
# A.AND(B).execute()

Expression(A).AND(Expression(B).AND(A)).OR(Expression(C).XOR(Expression(A).OR(D))).compile()