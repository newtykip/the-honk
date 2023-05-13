from math import log, floor

class Memoize:
    """Helper class to memoize a decorated function."""
    def __init__(self, function):
        self.function = function
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.function(*args)
        return self.memo[args]

@Memoize
def pdi(power: int, base: int, number: int) -> int:
    """Computes the perfect digital invariant."""
    return sum(pow((number % pow(base, i + 1) - number % pow(base, i)) / pow(base, i), power) for i in range(0, floor(log(number, base)) + 1))

def isHappy(number: int, base: int = 10) -> bool:
    """Check if a number is happy in a given base. Defaults to base 10."""
    seen = set()

    while number > 1 and number not in seen:
        seen.add(number)
        number = pdi(2, base, number)

    return number == 1

print(isHappy(19))