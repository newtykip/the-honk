from typing import List, Any

def reverse(arr: List[Any]):
    if not arr:
        return []

    x, y = arr[0], arr[1:]
    return reverse(y) + [x]

print(reverse([5,3,1]))