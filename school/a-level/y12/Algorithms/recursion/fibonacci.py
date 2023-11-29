from timeit import timeit
from random import randint
from functools import wraps

TRIAL_COUNT = 100
n = randint(2, 20)

# non-memoized
def fib(n):
    if n in {0, 1}:
        return n

    return fib(n - 1) + fib(n - 2)

# memoized
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

memo_fib = memoize(fib)

# output
a = fib(n)
b = memo_fib(n)

assert a == b

time_a = timeit(lambda: fib(n), number=TRIAL_COUNT)
time_b = timeit(lambda: memo_fib(n), number=TRIAL_COUNT)
time_diff = time_a - time_b

print(f"""fib({n}) = {a}
non-memo: {time_a} seconds
memo: {time_b} seconds

difference of {time_diff} seconds ({round(time_diff / time_a * 100, 3)}% of non-memo)""")