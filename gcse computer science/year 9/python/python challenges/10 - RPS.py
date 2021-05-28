import random

# 0: rock
# 1: paper
# 2: scissors
rps = ['rock', 'paper', 'scissors']

cpu = random.randint(0, 2)

user = str.lower(input('Rock, paper, or scissors?'))
user = rps.index(user)

print('Computer: ', rps[cpu])
print('User: ', rps[user])

# if it is a tie
if ((cpu == 0) & (user == 0)) | ((cpu == 1) & (user == 1)) | ((cpu == 2) & (user == 2)):
    print('It was a tie!')
    exit()
# if the computer wins
elif ((cpu == 1) & (user == 0)) | ((cpu == 0) & (user == 2)) | ((cpu == 2) & (user == 1)):
    print('Computer wins!')
else:
    print('User wins!')
