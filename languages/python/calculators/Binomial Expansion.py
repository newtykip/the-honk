# (a + b) ^ n
superscript = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

while True:
    try:
        n = int(input('Please enter a power to put (a + b) to! '))
        break
    except ValueError:
        print('The power must be a valid integer!')
        continue

terms = []

for r in range(n + 1):
    a = n - r
    b = r
    c = int(nCr(n, r))
    term = ''

    if c != 1:
        term += str(c)

    if a != 0:
        term += 'a'
        if a != 1:
            power = ''
            for digit in str(a):
                power += superscript[int(digit)]
            term += power

    if b != 0:
        term += 'b'
        if b != 1:
            power = ''
            for digit in str(b):
                power += superscript[int(digit)]
            term += power

    terms.append(term)

print(' + '.join(terms))