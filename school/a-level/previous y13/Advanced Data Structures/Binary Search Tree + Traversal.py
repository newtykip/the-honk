from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Tuple, List

T = TypeVar("T")

@dataclass
class Node(Generic[T]):
    data: T
    left: Node[T] = None
    right: Node[T] = None

class BST(Generic[T]):
    """Full implementation of a Binary Search Tree"""

    def __init__(self):
        self.__root: Node[T] = None

    def findMinimum(self) -> Node[T]:
        """Find the minimum node in the tree."""
        current = self.__root

        # Keep traversing left when possible - smaller numbers will always be on the left!
        while current.left:
            current = current.left

        return current

    def findMaximum(self) -> Node[T]:
        """Find the maximum node in the tree."""
        current = self.__root

        # Keep traversing right when possible - larger numbers will always be on the right!
        while current.right:
            current = current.right

        return current

    def insert(self, data: T) -> BST[T]:
        """Inserts a new piece of data into the tree."""
        node = Node(data)

        if self.__root == None:
            # Ensure there is a root node in the first place!
            self.__root = node
            return self
        else:
            current = self.__root
            parent = None

            while True:
                parent = current

                # If the currently selected node has a greater value than the newly created node, move left to a smaller valued node
                if node.data < current.data:
                    current = current.left

                    # If there is no node to the left, insert the newly made node!
                    if current == None:
                            parent.left = node
                            return self
                # Do the same thing but to the right if the selected node has a lesser value than the newly created node.
                else:
                    current = current.right

                    if current == None:
                        parent.right = node
                        return self

    def getNodeWithParent(self, data: T) -> Tuple[Node[T], Node[T]]:
        """Find a node containing the data point, and return it alongside its parent. Returns (parent, child)"""
        parent = None
        current = self.__root

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
                current = current.left
            # Otherwise, traverse right!
            else:
                parent = current
                current = current.right

    def remove(self, data: T) -> BST[T]:
        parent, node = self.getNodeWithParent(data)

        # If there is no node with that data, just do nothing
        if parent == None and node == None:
            return self

        # Determine the amount of children that the node has
        childrenCount = 0

        if node.left and node.right:
            childrenCount = 2
        elif (node.left == None) and (node.rightChild == None):
            childrenCount = 0
        else:
            childrenCount = 1

        # Remove the node from the tree
        if childrenCount == 0:
            if parent:
                if parent.right == node:
                    parent.right = None
                else:
                    parent.left = None
            else:
                self.__root = None
        elif childrenCount == 1:
            nextNode = None

            if node.left:
                nextNode = node.left
            else:
                nextNode = node.right

            if parent:
                if parent.left == node:
                    parent.left = nextNode
                else:
                    parent.right = nextNode
            else:
                self.__root = nextNode  
        else:
            leftmostParent = node
            leftmostNode = node.right

            while leftmostNode.left:
                leftmostParent = leftmostNode
                leftmostNode = leftmostNode.left

            node.data = leftmostNode.data

            if leftmostParent.left == leftmostNode:
                leftmostParent.left = leftmostNode.rightChild
            else:
                leftmostNode.rightChild = leftmostNode.rightChild

    def search(self, data: T) -> T:
        """Search through the binary tree. Returns the data value if found, otherwise returns None."""
        current = self.__root

        while True:
            # If the final node has been reached, return None
            if current == None:
                return None
            # If the node has been found, return the data!
            elif current.data == data:
                return data
            # If the currently selected node has a higher value than the data being searched for, traverse left
            elif current.data > data:
                current = current.left
            # Otherwise, traverse right
            else:
                current = current.right

    def rootNode(self) -> Node[T]:
        return self.__root

    @staticmethod
    def inOrder(root: Node[T] | BST[T]) -> List[T]:
        if isinstance(root, BST):
            root = root.rootNode()

        out = []
        
        if root:
            out = BST.inOrder(root.left)
            out.append(root.data)
            out = out + BST.inOrder(root.right)

        return out
        
    @staticmethod
    def preOrder(root: Node[T] | BST[T]) -> List[T]:
        if isinstance(root, BST):
            root = root.rootNode()

        out = []

        if root:
            out.append(root.data)
            out = out + BST.preOrder(root.left)
            out = out + BST.preOrder(root.right)

        return out

    @staticmethod
    def postOrder(root: Node[T] | BST[T]) -> List[T]:
        if isinstance(root, BST):
            root = root.rootNode()

        out =[]

        if root:
            out = BST.postOrder(root.left)
            out = out + BST.postOrder(root.right)
            out.append(root.data)

        return out

tree = BST[int]()

tree.insert(12).insert(14).insert(8).insert(2).insert(8).insert(7).insert(23).insert(19).insert(6).insert(22)

print(tree.postOrder(tree.rootNode()))