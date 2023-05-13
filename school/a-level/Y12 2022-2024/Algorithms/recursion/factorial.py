def recursive_factorial(n):
    if n == 1:
        return 1

    return n * recursive_factorial(n - 1)

def iterative_factorial(n):
    out = 1

    for i in range(2, n + 1):
        out *= i

    return out

assert iterative_factorial(5) == recursive_factorial(5)