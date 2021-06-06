import os
import re

pieces = {
    'w': {
        'K': '\u2654',
        'Q': '\u2655',
        'R': '\u2656',
        'B': '\u2657',
        'N': '\u2658',
        'P': '\u2659'
    },
    'b': {
        'K': '\u265A',
        'Q': '\u265B',
        'R': '\u265C',
        'B': '\u265D',
        'N': '\u265E',
        'P': '\u265F'
    }
}

filename = input('Enter the name of the .pgn file! ')
dir = os.path.dirname(os.path.realpath(__file__))
file = open('{0}/{1}.pgn'.format(dir, filename))
lines = file.readlines() # Read all lines

indexOfTurnOne = lines.index([s for s in lines if '1. ' in s][0]) # Find the index of move one
turns = lines[indexOfTurnOne:len(lines)] # Find the beginning of the turns
turns = re.findall(" ".join(["[^ ]+"] * 3), ' '.join(turns)) # Split on every third space
turns = list(map(lambda s: s.replace('\n', ''), turns)) # Remove all new lines from turns

for turn in turns:
    i = turns.index(turn)
    turns[i] = {
        'number': int(turn.split('.')[0]),
        'moves': {
            'w': {
                'move': turn.split('.')[1].strip().split(' ')[0]
            },
            'b': {
                'move': turn.split('.')[1].strip().split(' ')[1]
            }
        }
    }

    for side in turns[i]['moves']:
        print(turns[i]['moves'][side])
        if turns[i]['moves'][side]['move'][0].islower():
            turns[i]['moves'][side]['piece'] = 'P'
        elif turns[i]['moves'][side]['move'][0] == 'R' or turns[i]['moves'][side]['move'][0].startswith('O'):
            turns[i]['moves'][side]['piece'] = 'R'
        else:
            turns[i]['moves'][side]['piece'] = turns[i]['moves'][side]['move'][0]
    
    print(turns[i])

board = [
    ['bR','bN','bB''bQ','bK','bB','bN','bR'],
    ['bP','bP','bP','bP','bP','bP','bP','bP'],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['wP','wP','wP','wP','wP','wP','wP','wP'],
    ['wR','wN','wB''wQ','wK','wB','wN','wR']
]

def render(turn):
    global board
    i = turns.index(turn)
    for colour in turns[i]['moves']:
        move = turns[i]['moves'][colour]['move']
        if len(move) == 2:
            for row in board:
                for file in row:
                    if file == '{0}{1}'.format(colour, turns[i]['moves'][colour]['piece']):
                        print('a', )
   
    return board
            
print(render(turns[0]))