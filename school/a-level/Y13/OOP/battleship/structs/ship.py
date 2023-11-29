from typing import Tuple
from enum import Enum
from dataclasses import dataclass
import structs.player as player
import structs.board as board

@dataclass
class TypeInfo:
    """Describes a ship type."""
    name: str
    size: int
    quantity: int

class ShipType(Enum):
    """An enum describing all of the default ship types."""
    BATTLE = TypeInfo("Battle", 5, 1)
    CRUISER = TypeInfo("Cruiser", 4, 1)
    SUBMARINE = TypeInfo("Submarine", 3, 1)
    DESTROYER = TypeInfo("Destroyer", 2, 1)
    SPY = TypeInfo("Spy", 1, 4)

class Orientation(Enum):
    """Describes the orientation of a ship."""
    HORIZONTAL = 1
    VERTICAL = 2

class Ship:
    """
    Shared functionality between all types of ship.

    Attributes:
        __info (TypeInfo): Information about the ship.
        __x (int): The x-coordinate which the ship starts at.
        __y (int): The y-coordinate which the ship starts at.
        __orientation (Orientation): The orientation of the ship on the board.
        __owner (PlayerCardinal): The cardinal associated with the player that owns the ship.
        __hits (bool[]): List of booleans that describes all of the hits on the ship.
    """

    def __init__(self, type: TypeInfo, position: Tuple[int, int], orientation: Orientation, owner: "player.PlayerCardinal"):
        self.__info: TypeInfo = type.value
        self.__x, self.__y = position
        self.__orientation = orientation
        self.__owner = owner
        self.__hits = [False for _ in range(self.__info.size)]

    def get_owner(self, board: "board.Board") -> player.Player:
        return board.players()[self.__owner - 1]

    def get_size(self) -> int:
        return self.__info.size

    def get_orientation(self) -> Orientation:
        return self.__orientation

    def has_sunk(self) -> bool:
        """Has the ship been sunk?"""
        return all(self.__hits)

    def get_position(self) -> Tuple[int, int]:
        """Returns a (x, y) coordinate pair representing the location of the ship."""
        return (self.__x, self.__y)