from functools import wraps

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

@memoize
def fib(n: int) -> int:
    if n in {0, 1}:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(6))