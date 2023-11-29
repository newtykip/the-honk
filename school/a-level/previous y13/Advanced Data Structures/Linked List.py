from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Iterable, Union, List

T = TypeVar("T")

@dataclass
class Node(Generic[T]):
    data: T
    next: Node[T] = None

    def __repr__(self) -> str:
        return str(self.data)

class LinkedList(Generic[T]):
    def __init__(self, initialValues: Iterable[T]):
        self.head: Node[T] = None
        self.tail: Node[T] = None

        self.extend(initialValues)

    def __iter__(self) -> Iterable[T]:
        """Traverse the linked list."""
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __getitem__(self, index: int) -> Node[T]:
        """Get an item by its index."""
        if index > len(self) - 1:
            raise IndexError("Out of bounds")

        for i, node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index: int, data: T):
        """Set an item by its index."""
        if index > len(self) - 1:
            raise IndexError("Out of bounds")

        for i in range(len(self)):
            if i == index:
                self[i].data = data
                break

    def __delitem__(self, index: int):
        """Delete an item using its index."""
        if index > len(self) - 1:
            raise IndexError("Out of bounds")

        for i in range(len(self)):
            if i == index:
                for j in range(1, len(self) - i):
                    self[i + j - 1] = self[i + j].data

                self[len(self) - 2].next = None
                break

    def __add__(self, data: Union[T, List[T], LinkedList[T]]) -> LinkedList[T]:
        copy = self.copy()

        if isinstance(data, LinkedList) or type(data) == list:
            return copy.extend(iter(data) if type(data) == list else iter(map(lambda x: x.data, data)))
        else:
            return copy.append(data)

    def __len__(self) -> int:
        """Get the length of the linked list."""
        count = 0

        for _ in self:
            count += 1

        return count

    def append(self, value: T) -> LinkedList[T]:
        """Append data to the end of the linked list."""
        node = Node(value)

        if self.head is None:
            self.head = node
            return self

        for currentNode in self:
            pass

        currentNode.next = node

        return self

    def clear(self) -> LinkedList[T]:
        """Clear the linked list."""
        self.head = None
        self.tail = None
        return self

    def count(self, value: T) -> int:
        """Count the number of occurrences of a value."""
        count = 0

        for node in self:
            if node.data == value:
                count += 1

        return count

    def extend(self, iterable: Iterable[T]) -> LinkedList[T]:
        """Extend the list from an iterable."""
        for value in iterable:
            self.append(value)

        return self

    def index(self, value: T) -> int:
        """Finds the first index of a value. Returns -1 if the value is not in the list."""
        for i, node in enumerate(self):
            if node.data == value:
                return i

        return -1

    def insert(self, index: int, value: T) -> LinkedList[T]:
        """Inserts a value before an index."""
        if index > len(self) - 1:
            raise IndexError("Out of bounds")

        for i in range(len(self)):
            if i == index:
                container = value

                for j in range(len(self)):
                    try:
                        temp = self[i + j].data
                        self[i + j].data = container
                        container = temp
                    except IndexError:
                        self.append(container)

                break

        return self

    def pop(self) -> Node[T]:
        """Pop and return the final element of the list."""
        for node in self:
            pass

        del self[len(self) - 1]

        return node

    def remove(self, value: T) -> LinkedList[T]:
        for i, node in enumerate(self):
            if node.data == value:
                del self[i]
                return self

        raise ValueError("Value not found")

    def copy(self) -> LinkedList[T]:
        """Returns a copy of the list."""
        return LinkedList[T](iter(map(lambda x: x.data, self)))

    def sort(self) -> LinkedList[T]:
        n = len(self)
        swapped = False

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self[j].data > self[j + 1].data:
                    swapped = True
                    self[j], self[j + 1] = self[j + 1].data, self[j].data

            if not swapped:
                break

        return self

    def __repr__(self) -> str:
        out = "["

        for i, node in enumerate(self):
            value = node.data

            out += f'"{value}"' if type(value) == str else value

            if i != len(self) - 1:
                out += ", "

        return out + "]"

names = LinkedList[str](["Jacob", "Janet"])
names.extend(["Alfred", "Sophie"]).insert(1, "John Snow")
names.remove("Alfred")
names += "Woody"
names.sort()

print(names)
