from typing import List, TypeVar

T = TypeVar('T')

def select(arr: List[T], low: int, high: int, n: int):
	while True:
		print('a')
		if low == high:
			return low
		
		pivot_index = get_pivot(arr, low, high)
		pivot_index = partition(arr, low, high, pivot_index, n)

		if n == pivot_index:
			return n
		elif n < pivot_index:
			high = pivot_index - 1
		else:
			low = pivot_index + 1

def partition(arr: List[T], low: int, high: int, pivot_index: int, n: int) -> int:
	pivot_value = arr[pivot_index]
	arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
	store_index = low

	for i in range(low, high):
		if arr[i] < pivot_value:
			arr[store_index], arr[i] = arr[i], arr[store_index]
			store_index += 1
	
	store_index_eq = store_index

	for i in range(store_index, high):
		if arr[i] == pivot_value:
			arr[store_index_eq], arr[i] = arr[i], arr[store_index_eq]
			store_index_eq += 1

	arr[high], arr[store_index_eq] = arr[store_index_eq], arr[high]

	if n < store_index:
		return store_index
	elif n <= store_index_eq:
		return n
	
	return store_index_eq

def partition5(arr: List[T], low: int, high: int) -> int:
	i = low + 1

	while i <= high:
		j = i

		while j > low and arr[j - 1] > arr[j]:
			arr[j - 1], arr[j] = arr[j], arr[j - 1]
			j -= 1
		
		i += 1

	return (low + high) // 2

def get_pivot(arr: List[T], low: int, high: int) -> int:
	if high - low < 5:
		return partition5(arr, low, high)

	for i in range(low, high + 1, 5):
		sub_high = i + 4

		if sub_high > high:
			sub_high = high

		median5 = partition5(arr, i, sub_high)
		arr[median5], arr[low + (i - low) // 5] = arr[low + (i - low) // 5], arr[median5]

	mid = (high - low) / 10 + low + 1

	return select(arr, low, low + (high - low) // 5, mid)

# https://en.wikipedia.org/wiki/Quicksort
def recursive_quick_sort(arr: List[T], asc: bool = True, low: int = 0, high: int = None) -> List[T]:
	if high is None or high > len(arr) - 1:
		high = len(arr) - 1
	
	if low < high:
		# pivot = arr[high]
		pivot = get_pivot(arr, low, high)
		i = low - 1

		for j in range(low, high):
			if arr[j] <= pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		
		arr[i + 1], arr[high] = arr[high], arr[i + 1]
		 
		recursive_quick_sort(arr, asc, low, i)
		recursive_quick_sort(arr, asc, i + 2, high)
		
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
