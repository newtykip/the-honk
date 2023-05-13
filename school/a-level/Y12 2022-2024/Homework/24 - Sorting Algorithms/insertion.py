from typing import List, TypeVar

T = TypeVar('T')

# optimised implementation of insertion sort, psuedocode from https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(arr: List[T], asc: bool = True) -> List[T]:
	i = 1

	while i < len(arr):
		x = arr[i]
		j = i - 1

		while j >= 0 and arr[j] > x:
			arr[j + 1] = arr[j]
			j -= 1
		
		arr[j + 1] = x
		i += 1
	
	return arr if asc else arr[::-1]
