from random import randint

class Dice:
    # Initialise the class - make the default amount of sides 6
    def __init__(self, sides=6):
        self.sides = sides

    # Roll the dice once - return an integer
    def roll(self):
        return randint(1, self.sides)

class Player:
    # Initialise the class - create a dice and initialise the score parameter
    def __init__(self, id, dice):
        self.id = id
        self.dice = dice
        self.score = 0
        self.rolls = []

    # Roll the dice a specified amount of times - return an array of integers
    def rollMany(self, times):
        for i in range(times):
            num = self.dice.roll()
            self.rolls.append(num)

    def reset(self):
        self.rolls = []
        self.score = 0

class Game:
    def __init__(self, *player):
        self.players = player

    def determineWinner(self):
        scores = {}
        for i in self.players:
            i.score = sum(i.rolls)
            scores[i.id] = i.score
        highestScore = max(scores.values())
        for player, score in scores.items():
            if score == highestScore:
                if list(scores.values()).count(highestScore) > 1:
                    drew = []
                    for i in self.players:
                        if i.score == highestScore:
                            drew.append(str(i.id))
                    print("Players {0} have drawn first place with {1} score!".format(', '.join(drew), highestScore))
                else:
                    playerInfo = self.players[player - 1]
                    print("Player {0} wins with {1} score!".format(player, playerInfo.score))
                break

dice = Dice()
p1 = Player(1, dice)
p2 = Player(2, dice)
p1.rollMany(6)
p2.rollMany(6)

game = Game(p1, p2)
game.determineWinner()