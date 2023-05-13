import functools
import inspect
from copy import copy
from typing import Callable

def curry(function: Callable) -> Callable:
	# call functools.partial recursively in order to curry a function
	def inner(*args, **kwargs):
		partial = functools.partial(function, *args, **kwargs)
		signature = inspect.signature(partial.func)

		try:
			signature.bind(*partial.args, **partial.keywords)
		except TypeError:
			return curry(copy(partial)) # there must be more arguments to curry
		else:
			return partial()

	return inner

def add(a, b):
    return a + b

x = curry(add)(2)
print(x)