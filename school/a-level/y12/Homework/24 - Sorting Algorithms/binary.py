from typing import List, TypeVar

T = TypeVar('T')

def binary_search(arr: List[T], target: T) -> int:
	n = len(arr)
	l = 0
	r = n - 1
	
	while l <= r:
		m = (l + r) // 2

		if arr[m] < target:
			l = m + 1
		elif arr[m] > target:
			r = m - 1
		else:
			return m
		
	return -1
