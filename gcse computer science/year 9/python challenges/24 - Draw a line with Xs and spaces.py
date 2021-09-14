def drawLine(spaces, xs):
    string = '';

    for space in range(spaces):
        string = string + ' ';
    for x in range(xs):
        string = string + 'x';

    print(string)

# draw an egg
drawLine(5,7)
drawLine(4,9)
drawLine(3,11)
drawLine(4,9)
drawLine(5,7)