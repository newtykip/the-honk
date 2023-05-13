from typing import List, TypeVar

T = TypeVar('T')

def partition(arr: List[T], low: int, high: int) -> int:
	pivot = arr[high]
	i = low - 1

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	
	arr[i + 1], arr[high] = arr[high], arr[i + 1]

	return i + 1

# https://en.wikipedia.org/wiki/Quicksort
def recursive_quick_sort(arr: List[T], asc: bool = True, low: int = 0, high: int = None) -> List[T]:
	if high is None or high > len(arr) - 1:
		high = len(arr) - 1
	
	if low < high:
		p = partition(arr, low, high)
		 
		recursive_quick_sort(arr, asc, low, p - 1)
		recursive_quick_sort(arr, asc, p + 1, high)
		
		return arr if asc else arr[::-1]
	
def iterative_quick_sort(arr: List[T], asc: bool = True, low: int = 0, high: int = None) -> List[T]:
	if high is None or high > len(arr) - 1:
		high = len(arr) - 1
	
	if low < high:
		size = high - low + 1
		stack = [0] * size
		top = -1

		top += 1
		stack[top] = low
		top += 1
		stack[top] = high

		while top >= 0:
			high = stack[top]
			top -= 1
			low = stack[top]
			top -= 1

			p = partition(arr, low, high)

			if p - 1 > low:
				top += 1
				stack[top] = low
				top += 1
				stack[top] = p - 1
				
			if p + 1 < high:
				top += 1
				stack[top] = p + 1
				top += 1
				stack[top] = high
		
		return arr if asc else arr[::-1]
