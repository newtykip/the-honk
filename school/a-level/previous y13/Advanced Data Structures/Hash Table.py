from typing import Generic, TypeVar
from math import ceil

K, V = TypeVar('K'), TypeVar('V')

class HashItem(Generic[K, V]):
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value

class HashTable(Generic[K, V]):
    def __init__(self):
        self.__size = 256
        self.__count = 0
        self.__slots: list[HashItem[K, V]] = [None for _ in range(self.__size)]

    def __hash(self, key: K):
        multiplier = 1
        hashValue = 0

        for character in key:
            hashValue += multiplier * ord(character)
            multiplier += 1
        
        return hashValue % self.__size
        
    def __filledSlots(self):
        return list(filter(lambda x: x is not None, self.__slots))

    def __load(self):
        return len(list(self.__filledSlots())) / self.__size

    def __grow(self, newSize: int):
        self.__slots += [None for _ in range(newSize - self.__size)]
        self.__size = newSize

    def put(self, key: K, value: V):
        item = HashItem(key, value)
        hashValue = self.__hash(key)

        while self.__slots[hashValue] != None:
            if self.__slots[hashValue].key == key:
                break
                
            hashValue += 1
            hashValue %= self.__size
        
        if self.__slots[hashValue] == None:
            self.__count += 1

        # If the hash table is nearing its maximum load, increase the size of the hash table by 10%
        if self.__load() >= 0.75:
            self.__grow(ceil(self.__size * 1.1))
        
        self.__slots[hashValue] = item

    def get(self, key: K):
        hashValue = self.__hash(key)

        for slot in self.__filledSlots():
            if hashValue == self.__hash(slot.key):
                return slot.value
        
        return None

    def __setitem__(self, key: K, value: V):
        self.put(key, value)

    def __getitem__(self, key: K):
        return self.get(key)

    def __str__(self):
        template = " {: ^10}  |  {: ^10}"
        out = template.format("Key", "Value")
        out += "\n" + ("-" * (len(out) // 2)) + "|" + ("-" * (len(out) // 2)) + "\n"

        slots = self.__filledSlots()

        for i, slot in enumerate(slots):
            out += template.format(slot.key, slot.value)

            if i + 1 != len(slots):
                out += "\n"

        return out
    
    def __len__(self):
        return len(self.__slots)

ages = HashTable[str, int]()
ages["Jacob"] = 16
print(ages)
