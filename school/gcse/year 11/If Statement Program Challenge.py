import random
import time

# A class to represent a fair n-sided dice
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

# A class to represent the player
class Player:
    def __init__(self):
        self.dice = Dice(6)
        self.score = 0

    def roll(self):
        return self.dice.roll()

# Enum to represent the result of the end of the game
### 0 - Tie
### 1 - Player One wins!
### 2 - Player Two wins!
class GameResult:
    Tie = 0
    PlayerOne = 1
    PlayerTwo = 2

# Initialise key variables for the game
playerOne = Player()
playerTwo = Player()
currentRound = 0

# Play a round of the game
def play():
    global currentRound

    # Increment the round and roll the dice
    currentRound += 1
    playerOneRoll = playerOne.roll()
    playerTwoRoll = playerTwo.roll()

    # Figure out the result of the game
    if playerOneRoll > playerTwoRoll:
        playerOne.score += 1
        state = GameResult.PlayerOne
    elif playerOneRoll == playerTwoRoll:
        state = GameResult.Tie
    else:
        playerTwo.score += 1
        state = GameResult.PlayerTwo

    # Turn the result of the game into a string
    if state == GameResult.Tie:
        header = 'Round %i was a tie' % (currentRound)
    elif state == GameResult.PlayerOne:
        header = 'Player One wins Round %i' % (currentRound)
    elif state == GameResult.PlayerTwo:
        header = 'Player Two wins Round %i' % (currentRound)

    # Print a summary of the end of the round
    print("""

%s! The current scores are as follows:

Player One - %i
Player Two - %i""" % (header, playerOne.score, playerTwo.score)
    )

# Keep playing until someone has won three rounds
while playerOne.score != 3 and playerTwo.score != 3:
    play() # Play the round
    time.sleep(2) # Pause for two seconds to allow for time for the user to read the summary