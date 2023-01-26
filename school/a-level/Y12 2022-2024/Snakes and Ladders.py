from enum import Enum
from random import randint
from math import sqrt
from uuid import uuid1

BOARD_SIZE = 8
TOTAL_SNAKES = 10
TOTAL_LADDERS = 10

MIN_MAGNITUDE = 2
MAX_MAGNITUDE = 4

class TileType(Enum):
    Empty = 0
    Snake = 1
    Ladder = 2

def rollDice():
    return randint(1, 6)

def randomCoordinate(startX = 0, startY = 0):
    return (randint(startX, BOARD_SIZE - 1), randint(startY, BOARD_SIZE - 1))

def generateBoard(playerLocation):
    board = [[(TileType.Empty, None, False, uuid1()) for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    elements = TOTAL_SNAKES + TOTAL_LADDERS

    playerX, playerY = playerLocation
    board[playerY][playerX] = (TileType.Empty, None, True, board[playerY][playerX][3])

    usedCoords = [
        playerLocation,
        (playerX + 1, playerY)
    ]

    for i in range(elements):
        tileType = TileType.Snake if i<= TOTAL_SNAKES - 1 else TileType.Ladder
        generating = True

        while generating:
            startX, startY = randomCoordinate()
            endX, endY = randomCoordinate()
            magnitude = sqrt((startX - endX) ** 2 + (startY - endY) ** 2)

            if (
                        (startY != endY)
                and (magnitude < MAX_MAGNITUDE)
                and (magnitude > MIN_MAGNITUDE)
                and ((startX, startY) not in usedCoords)
                and ((endX, endY) not in usedCoords)
            ):
                generating = False

        board[startY][startX] = (tileType, i, board[startY][startX][2], board[startY][startX][3])
        board[endY][endX] = (tileType, i, board[startY][startX][2], board[endY][endX][3])

        usedCoords.append((startX, startY))
        usedCoords.append((endX, endY))

    return board

def renderBoard(board):
    for row in board:
        for type, _, player, _ in row:
            colString = 'S' if type == TileType.Snake else 'L' if type == TileType.Ladder else 'P' if player  else '-'

            print(colString, end=' ')
        print()

def movePlayer(board, playerLocation):
    x, y = playerLocation
    newX = x
    newY = y

    # Curl around the board
    if y % 2 == 0:
        if newX == 0:
            newY -= 1
        else:
            newX -= 1
    else:
        if newX == BOARD_SIZE - 1:
            newY -= 1
        else:
            newX += 1

    cell = board[newY][newX]
    # Check for intersections with snakes or ladders
    if cell[0] == TileType.Snake:
        for i, row in enumerate(board):
            for col in row:
                if col[0] == TileType.Snake and col[1] == cell[1] and col[3] != cell[3]:
                    print(col)
                    if i < newY:
                        newY = i
                    
    board[y][x] = (board[y][x][0], board[y][x][1], False, board[y][x][3])
    board[newY][newX] = (board[newY][newX][0], board[newY][newX][1], True, board[newY][newX][3])

    return (board, (newX, newY))

playerLocation = (BOARD_SIZE - 1, BOARD_SIZE - 1)

board = generateBoard(playerLocation)
renderBoard(board)
print()

board, playerLocation = movePlayer(board, playerLocation)
renderBoard(board) 
print()

board, playerLocation = movePlayer(board, playerLocation)
renderBoard(board) 