from enum import Enum

class PlayerCardinal(Enum):
    """Describes the cardinal associated with the player."""
    ONE = 1
    TWO = 2

class Player:
    """
    A battleship player.
    
    Attributes:
        __nickname (str) - A nickname for the player.
        __games_played (int) - The number of games played by the player.
        __win_count (int) - The win count of the player.
    """

    def __init__(self, nickname: str):
        self.__nickname = nickname

        # todo: implement
        self.__games_played = 0
        self.__win_count = 0

    def win_rate(self) -> float:
        """Calculate the win rate for the player."""
        # prevent division by zero error
        try:
            return (self.__win_count / self.__games_played) * 100
        except:
            return 0