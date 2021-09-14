time = int(input('How long on average do you spend watching TV a day? (Please answer in minutes.)'))

if time <= 120:
    print('That shouldn\'t rot your brain too much.')
elif time <= 240:
    print('Aren\'t you getting square eyes?')
else:
    print('Fresh air beats channel flicking.')