import random

def generateList(minimum, maximum, length):
    res = []
    for i in range(length):
        res.append(random.randint(minimum, maximum))
    return res

def bubbleSort(data, asc = True):
    dataClone = data.copy()
    hasSwapped = True
    indexToCheck = len(dataClone) - 1
    while indexToCheck > 0 and hasSwapped:
        hasSwapped = False
        for i in range(indexToCheck):
            if asc and dataClone[i] > dataClone[i + 1] or not asc and dataClone[i] < dataClone[i + 1]:
                hasSwapped = True
                a, b = dataClone[i], dataClone[i + 1]
                dataClone[i] = b
                dataClone[i + 1] = a
        indexToCheck -= 1
    return dataClone

nums = generateList(0, 100, 15)
sortedAsc = bubbleSort(nums, True)
sortedDesc = bubbleSort(nums, False)

print("""
Original: %s
Ascending: %s
Descending: %s
""" % (str(nums), str(sortedAsc), str(sortedDesc)))