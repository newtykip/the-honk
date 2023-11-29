def intInput(name):
    while True:
        try:
            number = int(input(f'Please enter an integer for {name}: '))
            return number
        except ValueError:
            print('Please enter a valid integer.')

A = intInput('A')
B = intInput('B')
C = intInput('C')

if (A < B) or (B < C):
    A = B

print(A)
