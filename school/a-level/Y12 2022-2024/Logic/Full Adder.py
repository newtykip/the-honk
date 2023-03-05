from typing import List

def getInt():
    while True:
        try:
            value = int(input("Please enter a natural number: "))

            return value
        except ValueError:
            print("Please enter a valid natural number.")

def getBin(x: int) -> List[int]:
    return list(map(lambda x: int(x), bin(abs(x))[2:]))

def twosComplementToInt(bits: List[int]) -> int:
    sum = 0 if bits[0] == 0 else -(2 ** (len(bits) - 1))
    del bits[0]
    bits.reverse()

    for i in range(len(bits)):
        if bits[i] == 1:
            sum += 2 ** i

    return sum

def add(x: int, y: int) -> int:
    bits = max(len(bin(x)[2:]), len(bin(y)[2:])) + 1
    mask = int("1" * bits, 2)
    xBin = list(map(lambda x: int(x), ("0" if x >= 0 else "1") + bin(x & mask)[2:]))
    yBin = list(map(lambda x: int(x), ("0" if y >= 0 else "1") + bin(y & mask)[2:]))

    print(xBin, yBin)

    # Pad the shortner binary number
    while len(xBin) < bits:
        xBin.insert(0, 0)
    while len(yBin) < bits:
        yBin.insert(0, 0)

    # We add from right to left
    xBin.reverse(); yBin.reverse()

    # Iteratively apply the full adder
    cout = 0
    outBin = []

    for a, b in zip(xBin, yBin):
        sum = cout ^ (a ^ b)
        cout = (a & b) | (cout & ((~a & b) | (a & ~b)))
        outBin.append(sum)

    if x > 0 and y > 0: outBin.append(cout)

    # We read from left to right
    outBin.reverse()
    print(outBin)

    return twosComplementToInt(outBin)

def subtract(x: int, y: int) -> int:
    return add(x, -y)

def multiply(x: int, y: int) -> int:
    if x == 1:
        return y
    elif x == -1:
        return -y
    elif y == 1:
        return x
    elif y == -1:
        return -x

    sgn = -1 if (x > 0 and y < 0) or (y > 0 and x < 0) else 1
    product = 0

    for num in [abs(x) for _ in range(abs(y))]:
        product = add(product, num)

    return multiply(sgn, product)

x, y = getInt(), getInt()

# Compare the results
print(x + y, add(x, y))
