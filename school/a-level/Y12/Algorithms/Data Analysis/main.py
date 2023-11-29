from __future__ import annotations
import matplotlib.pyplot as plt

def parseValue(value: str):
    value = value.strip()

    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    elif len(value.split(".")) == 2:
        return float(value)
    elif value.isnumeric():
        return int(value)
    else:
        return value

class Data:
    def __init__(self, fileName: str):
        with open(fileName, "r") as file:
            out = [[parseValue(value) for value in line.strip().split(",")] for line in file.readlines()]
            self.__data = { header: lst for (header, lst) in zip(out[0], zip(*out[1::])) }

    def getHeaderData(self, header: str):
        """Get the data under a header, CaSe insensitive"""
        for realHeader in self.__data.keys():
            if header.lower() == realHeader.lower():
                return self.__data[realHeader]
        
        return None

def bubbleSort(lst: list, asc: bool = True) -> list:
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst if asc else lst[::-1]


def getHeights(data: Data, male: bool) -> tuple:
    heights = data.getHeaderData("height")
    males = data.getHeaderData("male")

    return [height for height, isMale in zip(heights, males) if male == isMale]

def meanHeight(data: Data, male: bool):
    heights = getHeights(data, male)
    return sum(heights) / len(heights)

sports = Data("sports_data.csv")
femaleHeights = bubbleSort(getHeights(sports, False))

plt.bar([i for i in range(len(femaleHeights))], femaleHeights)
plt.savefig('yes.png')
