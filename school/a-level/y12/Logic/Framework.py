from __future__ import annotations
from enum import Enum

class Gate(Enum):
    AND = '^'
    OR = '∨'
    XOR = '⊕'
    NAND = '↑'
    NOR = '↓'
    XNOR = '⊙'

class Symbol():
    def __init__(self, symbol, initialValue):
        self._symbol = symbol
        self._value = initialValue
        self._tree = []

    def setValue(self, newValue):
        self._value = newValue
        return self

    def AND(self, symbol: Symbol):
        self._tree.append((Gate.AND, symbol))
        return self

    def compute():
        

    def __str__(self):
        return self._symbol