import random

class Deck():
    def __init__(self, suits):
        self.cards = []
        self.suits = suits

    def generate(self):
        for suit in self.suits:
            for cardType in range(1, 14):
                formattedCard = ""

                if cardType == 1:
                    formattedCard += "Ace"
                elif cardType == 11:
                    formattedCard += "Jack"
                elif cardType == 12:
                    formattedCard += "Queen"
                elif cardType == 13:
                    formattedCard += 'King'
                else:
                    formattedCard += str(cardType)

                formattedCard += ' of %s' % (suit)
                self.cards.append(formattedCard)

    def shuffle(self):
        currentCards = self.cards
        shuffledCards = []

        while len(currentCards) > 0:
            pick = random.randint(0, len(currentCards) - 1)
            removedCard = currentCards.pop(pick)
            shuffledCards.append(removedCard)

        self.cards = shuffledCards

deck = Deck(["Spades", "Hearts", "Diamonds", "Clubs"])
print(deck.cards)
deck.generate()
print(deck.cards)
deck.shuffle()
print(deck.cards)