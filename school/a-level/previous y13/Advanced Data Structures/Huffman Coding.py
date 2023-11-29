from __future__ import annotations
from dataclasses import dataclass
from queue import Queue

@dataclass
class Node:
    character: str = None
    frequency: int = None
    left: Node = None
    right: Node = None

def buildTree(message: str):
    frequencies = { k: v for k, v in sorted([(i, message.count(i)) for i in set(message)], key = lambda x: x[1], reverse = True )}
    frequencies = list(frequencies.items())

    subtrees = Queue()
    
    for i in range(len(frequencies)):
        subtree = Node(None, sum(map(lambda x: x[1], frequencies[i:])))
        subtree.right = Node(frequencies[i][0], frequencies[i][1])
        subtrees.put(subtree)

    tree = subtrees.get()
    current = tree

    for _ in range(subtrees.qsize()):
        subtree = subtrees.get()
        current.left = subtree
        current = current.left

    return tree

def encode(message: str):
    tree = buildTree(message)
    print(tree)
    frequencies = { i: message.count(i) for i in set(message) }
    frequencies = { k: v for k, v in sorted(frequencies.items(), key = lambda x: x[1] )}

print(encode("Hello World"))
