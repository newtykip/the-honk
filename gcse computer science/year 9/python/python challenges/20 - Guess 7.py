def guess():
    num = int(input('Please input a number.'))

    if num == 7:
        print('Well done!')
        exit()
    else:
        print('Try again!')
        guess()

guess()