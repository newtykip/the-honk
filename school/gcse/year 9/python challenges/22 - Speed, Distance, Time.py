def speed(distance, time):
    return distance / time

distance = int(input('Please input the distance (in metres).'))
seconds = int(input('Please input the time (in seconds) that the journey was completed in.'))
print(speed(distance, seconds))