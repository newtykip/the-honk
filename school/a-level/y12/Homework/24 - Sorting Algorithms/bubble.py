from typing import List, TypeVar

T = TypeVar('T')

# optimised implementation of bubble sort, psuedocode from https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(arr: List[T], asc: bool = True) -> List[T]:
	n = len(arr)
	swapped = False

	while not swapped:
		for i in range(1, n):
			if arr[i - 1] > arr[i]:
				arr[i - 1], arr[i] = arr[i], arr[i - 1]
				swapped = True
				
	return arr if asc else arr[::-1]
