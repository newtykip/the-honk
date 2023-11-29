from dataclasses import dataclass
from typing import Dict, List

class VariableMismatchError(Exception):
    pass

@dataclass(frozen=True)
class Node:
    """Represents a row of a truth table"""
    variables: Dict[str, bool]
    value: bool

class KMap:
    def __init__(self, variables: List[str]):
        self.__nodes: List[Node] = []
        self.__variables = variables

    def addNode(self, node: Node):
        variableCount = len(self.__variables)
        nodeVariableCount = len(node.variables.keys())

        if variableCount < nodeVariableCount:
            raise VariableMismatchError(f"You tried assigning a node with {nodeVariableCount} variables to a K-Map that supports {variableCount} variables.")
        
        for variable, _ in node.variables:
            if variable not in self.__variables:
                raise VariableMismatchError(f"{variable} is not a variable in this K-Map!")

        self.__nodes.append(node)
        return self

map = [
    Node({
        "A": False,
        "B": False
    }, True),
    Node({
        "A": True,
        "B": False
    }, True),
    Node({
        "A": False,
        "B": True
    }, False),
    Node({
        "A": True,
        "B": True
    }, True),
]

print(map)