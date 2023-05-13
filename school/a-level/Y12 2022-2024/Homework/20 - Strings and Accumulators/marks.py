from typing import List
import os.path

class Class:
	def __init__(self, name: str, marks: List[int] = []):
		self.__name = name
		self.__marks = marks
		self.__marks.sort()
		
	def __add__(self, marks: int | List[int]):
		if type(marks) == int:
			self.__marks.append(marks)
		elif type(marks) == list:
			self.__marks.extend(marks)

		self.__marks.sort()

		return self
	
	def __iadd__(self, marks: int | List[int]):
		return self.__add__(marks)
	
	def __len__(self) -> int:
		return len(self.__marks)
	
	def __str__(self) -> str:
		return self.__name
	
	def mean(self) -> int:
		return sum(self.__marks) / len(self.__marks)
	
	def median(self) -> int:
		return self.__marks[len(self.__marks) // 2]
	
	def above_median(self) -> int:
		return len([mark for mark in self.__marks if mark > self.median()])
	
	def below_median(self) -> int:
		return len([mark for mark in self.__marks if mark < self.median()])
	
	def mode(self) -> int:
		return max(set(self.__marks), key=self.__marks.count)
	
	def save(self):
		name = self.__name.replace("/", "")
		with open(f"{name}.csv", "w") as file:
			file.write(",".join([str(mark) for mark in self.__marks]))

def get_class(name: str):
	sanitized_name = name.replace("/", "")
	marks = []

	if os.path.exists(f"{sanitized_name}.csv"):
		with open(f"{sanitized_name}.csv", "r") as file:
			marks += [int(mark) for mark in file.read().split(",")]
	else:
		while True:
			try:
				marks = [int(x) for x in input(f"Please enter a comma separated list of the marks for class {name}: ").split(",") if x != ""]
				break
			except ValueError:
				print("Please enter a valid list of marks.")
				pass

	_class = Class(name, marks)
	_class.save()

	return _class

cs1 = get_class("12/CS1")
cs2 = get_class("12/CS2")

highest_mean = "12/CS1" if cs1.mean() > cs2.mean() else "12/CS2"

print(f"""
12/CS1
-------
Mean: {cs1.mean()}
Median: {cs1.median()}
Mode: {cs1.mode()}
Above Median: {cs1.above_median()}
Below Median: {cs1.below_median()}

12/CS2
-------
Mean: {cs2.mean()}
Median: {cs2.median()}
Mode: {cs2.mode()}
Above Median: {cs2.above_median()}
Below Median: {cs2.below_median()}

{highest_mean} has the highest mean.
""")
