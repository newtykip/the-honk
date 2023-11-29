import structs.board as board
import structs.player as player
import structs.ship as ship

class Move:
    """
    Represents an individual move in the game.
    
    Attributes:
        __number (int): Which move in the game is this?"""
    move_number = 1

    def __init__(self):
        # assign the move a number
        self.__number = Move.move_number
        Move.move_number += 1

    def player(self, board: "board.Board") -> "player.Player":
        """Get the player associated with the move."""
        return board.players()[int(self.__number % 2 == 1)]