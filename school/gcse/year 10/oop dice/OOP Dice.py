from random import randint

class Dice:
    # Initialise the class - make the default amount of sides 6
    def __init__(self, sides=6):
        self.sides = sides

    # Roll the dice once - return an integer
    def roll(self):
        return randint(1, self.sides)

    # Roll the dice a specified amount of times - return an array of integers
    def rollMany(self, times):
        res = []
        for i in range(times):
            num = self.roll()
            res.append(num)
        return res

dice = Dice() # Create an instance of the class Dice

p1 = dice.rollMany(6) # Roll 6 dice for player 1
p2 = dice.rollMany(6) # Roll 6 dice for player 2
p1score = sum(p1) # Calculate player 1's score
p2score = sum(p2) # Calculate player 2's score

# Output player 1's rolls and score for the user to see
print("Player 1 rolls ({0})".format(p1score))

for i in p1:
    pos = p1.index(i) + 1
    print("{0}. {1}".format(pos, i))

# Output player 2's rolls and score for the user to see
print("\nPlayer 2 rolls ({0})".format(p2score))

for i in p2:
    pos = p2.index(i) + 1
    print("{0}. {1}".format(pos, i))

# Determine the winner
if p1score > p2score:
    print("\nPlayer 1 ({0}) wins by {1} points!".format(p1score, p1score - p2score))
elif p2score > p1score:
    print("\nPlayer 2 ({0}) wins by {1} points!".format(p2score, p2score - p1score))
else:
    print("\nDraw!")