from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Tuple

T = TypeVar("T")

@dataclass
class Node(Generic[T]):
    data: T
    leftChild: Node[T] = None
    rightChild: Node[T] = None

class BinarySearchTree(Generic[T]):
    """Full implementation of a Binary Search Tree"""

    def __init__(self):
        self.__rootNode: Node[T] = None

    def findMinimum(self) -> Node[T]:
        """Find the minimum node in the tree."""
        current = self.__rootNode

        # Keep traversing left when possible - smaller numbers will always be on the left!
        while current.leftChild:
            current = current.leftChild

        return current

    def findMaximum(self) -> Node[T]:
        """Find the maximum node in the tree."""
        current = self.__rootNode

        # Keep traversing right when possible - larger numbers will always be on the right!
        while current.rightChild:
            current = current.rightChild

        return current

    def insert(self, data: T) -> BinarySearchTree[T]:
        """Inserts a new piece of data into the tree."""
        node = Node(data)

        if self.__rootNode == None:
            # Ensure there is a root node in the first place!
            self.__rootNode = node
            return self
        else:
            current = self.__rootNode
            parent = None

            while True:
                parent = current

                # If the currently selected node has a greater value than the newly created node, move left to a smaller valued node
                if node.data < current.data:
                    current = current.leftChild

                    # If there is no node to the left, insert the newly made node!
                    if current == None:
                            parent.leftChild = node
                            return self
                # Do the same thing but to the right if the selected node has a lesser value than the newly created node.
                else:
                    current = current.rightChild

                    if current == None:
                        parent.rightChild = node
                        return self

    def getNodeWithParent(self, data: T) -> Tuple[Node[T], Node[T]]:
        """Find a node containing the data point, and return it alongside its parent. Returns (parent, child)"""
        parent = None
        current = self.__rootNode

        # If there is no root node, there is also no parent node
        if current == None:
            return (None, None)
        
        while True:
            # If the node containing the data has been found, return the (parent, child) pair!
            if current.data == data:
                return (parent, current)
            # If the selected node has a greater value than the one being searched for, traverse left!
            elif current.data > data:
                parent = current
                current = current.leftChild
            # Otherwise, traverse right!
            else:
                parent = current
                current = current.rightChild

    def remove(self, data: T) -> BinarySearchTree[T]:
        parent, node = self.getNodeWithParent(data)

        # If there is no node with that data, just do nothing
        if parent == None and node == None:
            return self

        # Determine the amount of children that the node has
        childrenCount = 0

        if node.leftChild and node.rightChild:
            childrenCount = 2
        elif (node.leftChild == None) and (node.rightChild == None):
            childrenCount = 0
        else:
            childrenCount = 1

        # Remove the node from the tree
        if childrenCount == 0:
            if parent:
                if parent.rightChild == node:
                    parent.rightChild = None
                else:
                    parent.leftChild = None
            else:
                self.__rootNode = None
        elif childrenCount == 1:
            nextNode = None

            if node.leftChild:
                nextNode = node.leftChild
            else:
                nextNode = node.rightChild

            if parent:
                if parent.leftChild == node:
                    parent.leftChild = nextNode
                else:
                    parent.rightChild = nextNode
            else:
                self.__rootNode = nextNode  
        else:
            leftmostParent = node
            leftmostNode = node.rightChild

            while leftmostNode.leftChild:
                leftmostParent = leftmostNode
                leftmostNode = leftmostNode.leftChild

            node.data = leftmostNode.data

            if leftmostParent.leftChild == leftmostNode:
                leftmostParent.leftChild = leftmostNode.rightChild
            else:
                leftmostNode.rightChild = leftmostNode.rightChild

    def search(self, data: T) -> T:
        """Search through the binary tree. Returns the data value if found, otherwise returns None."""
        current = self.__rootNode

        while True:
            # If the final node has been reached, return None
            if current == None:
                return None
            # If the node has been found, return the data!
            elif current.data == data:
                return data
            # If the currently selected node has a higher value than the data being searched for, traverse left
            elif current.data > data:
                current = current.leftChild
            # Otherwise, traverse right
            else:
                current = current.rightChild

tree = BinarySearchTree[int]()

for i in range(10):
    tree.insert(i)
    found = tree.search(i)
    print(found)