from random import randint, choice
from timeit import timeit
from matplotlib import pyplot as plt
from copy import copy
import sys

sys.setrecursionlimit(1500) # this is required to run the recursive quicksort, but is usually not recommended

from linear import linear_search
from binary import binary_search
from bubble import bubble_sort
from insertion import insertion_sort
from quicksort import recursive_quick_sort, iterative_quick_sort

# config
LOW = 0
HIGH = 100
TRIAL_COUNT = 10
N_LIST = [50, 100, 1000]

times = {'Linear Search': [], 'Binary Search': [], 'Bubble Sort': [], 'Insertion Sort': [], 'Quicksort (Recursive)': [], 'Quicksort (Iterative)': []}
N_LIST.sort()

for n in N_LIST:
    # generate the test data
	data = [randint(LOW, HIGH) for _ in range(n)]
	random_element = choice(data)

	sorted_data = copy(data)
	sorted_data.sort()

	# perform all of the computations
	linear_time = round(timeit(lambda: linear_search(data, random_element), number=TRIAL_COUNT) * 1000, 4)
	binary_time = round(timeit(lambda: binary_search(sorted_data, random_element), number=TRIAL_COUNT) * 1000, 4)
	bubble_time = round(timeit(lambda: bubble_sort(data), number=TRIAL_COUNT) * 1000, 4)
	insertion_time = round(timeit(lambda: insertion_sort(data), number=TRIAL_COUNT) * 1000, 4)
	quicksort_recursive_time = round(timeit(lambda: recursive_quick_sort(data), number=TRIAL_COUNT) * 1000, 4)
	quicksort_iterative_time = round(timeit(lambda: iterative_quick_sort(data), number=TRIAL_COUNT) * 1000, 4)

	print(f"""n = {n}
Linear Search: {linear_time}ms
Binary Search: {binary_time}ms
Bubble Sort: {bubble_time}ms
Insertion Sort: {insertion_time}ms
Recursive Quicksort: {quicksort_recursive_time}ms
Iterative Quicksort: {quicksort_iterative_time}ms
-------------------------------------""")
	
	# store the times
	times['Linear Search'].append(linear_time)
	times['Binary Search'].append(binary_time)
	times['Bubble Sort'].append(bubble_time)
	times['Insertion Sort'].append(insertion_time)
	times['Quicksort (Recursive)'].append(quicksort_recursive_time)
	times['Quicksort (Iterative)'].append(quicksort_iterative_time)

# plot the times
plt.xlabel('n')
plt.ylabel('Time (ms)')

for key in times:
	plt.clf()
	plt.title(f"Time Complexity of {key}")
	print(key, times[key])
	plt.plot(N_LIST, times[key], linestyle='--', marker='o', color='b')
	plt.savefig(f"{key}.png")
