def ask():
    inp = str.lower(input('Please input an olympic value.'))

    if (inp == 'respect') | (inp == 'excellence') | (inp == 'friendship'):
        print('That\'s correct!')
        exit()
    else:
        print('Try again!')
        ask()

ask()