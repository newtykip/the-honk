from enum import Enum
from random import randint

# Enums
class Suit(Enum):
    Heart = 'Hearts'
    Club = 'Clubs'
    Diamond = 'Diamonds'
    Spade = 'Spades'

class CardTypes(Enum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    King = 10
    Queen = 10
    Jack = 10
    Ace = 11 # set this to none once ace picking logic is done (:, just allows totalValue to work

class DrawCardResults(Enum):
    Success = 0
    Fail = 1
    Ace = 2

# Classes
class Card:
    def __init__(self, cardType: CardTypes, suit: Suit):
        self.__suit = suit.value
        self.__type = cardType.name
        self.__value = cardType.value

    def __str__(self):
        return f'{self.__type} of {self.__suit}'

    def getValue(self):
        return self.__value

    def setValue(self, newValue: int):
        if self.__value == None:
            self.__value = newValue

class Deck:
    def __init__(self):
        self.__remainingCards = 52

    def drawCard(self):
        if self.__remainingCards == 0: return (None, None)

        card = CardTypes._member_map_[CardTypes._member_names_[randint(0, len(CardTypes._member_names_) - 1)]]
        suit = Suit._member_map_[Suit._member_names_[randint(0, len(Suit._member_names_)) - 1]]
        self.__remainingCards -= 1

        return (card, suit)

class Hand:
    def __init__(self, deck: Deck):
        self.cards = []
        self.__deck = deck

    def drawCard(self):
        card, suit = self.__deck.drawCard()
        self.cards.append(Card(card, suit))

        return DrawCardResults.Success if card != None else DrawCardResults.Ace if card == CardTypes.Ace else DrawCardResults.Fail

    def totalValue(self):
        total = 0

        for card in self.cards:
            total += card.getValue()

        return total

class Player:
    count = 0

    def __init__(self, deck: Deck, name: str = ''):
        Player.count += 1

        self.name = name if len(name) > 0 else f'Player {Player.count}'
        self.__hand = Hand(deck)

    def __str__(self):
        return self.__name

# Game
deck = Deck()
player = Player(deck)
player2 = Player(deck)