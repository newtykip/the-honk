from typing import List, TypeVar

T = TypeVar('T')

def linear_search(arr: List[T], target: T) -> int:
	for i in range(len(arr)):
		if arr[i] == target:
			return i
	
	return -1
