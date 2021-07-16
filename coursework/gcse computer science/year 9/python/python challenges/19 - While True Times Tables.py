while True:
    num = int(input('Please input a number'))

    for i in range(12):
        i = i + 1
        print(str(num) + ' * ' + str(i) + ' = ', str(num * i))