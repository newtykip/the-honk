from typing import List
import structs.player as player
import structs.ship as shipM
import structs.move as moveM

class Board:
    """
    The board on which the game is played.
    
    Attributes:
        __p1 (Player): Player one.
        __p2 (Player): Player two.
        __ships (Ship[]): All of the ships associated with the game.
        __moves (Move[]): All of the moves associated with the game.
    """
    SIZE = 8

    def __init__(self, player_one: "player.Player", player_two: "player.Player"):
        self.__p1 = player_one
        self.__p2 = player_two
        self.__ships: List["shipM.Ship"] = []
        self.__moves: List["moveM.Move"] = []
        self.__current_move = moveM.Move()

    def new_move(self):
        self.__moves.append(self.__current_move)
        self.__current_move = moveM.Move()

    def is_occupied(self, x: int, y: int) -> bool:
        """Are the provided coordinates occupied?"""
        for ship in self.__ships:
            ship_x, ship_y = ship.get_position()
            orientation = ship.get_orientation()

            for i in range(ship.get_size()):
                if (orientation == shipM.Orientation.HORIZONTAL and x == ship_x + i and y == ship_y) or (orientation == shipM.Orientation.VERTICAL and x == ship_x and y == ship_y + i):
                    return True

        return False

    def add_ship(self, ship: "shipM.Ship") -> bool:
        ship_x, ship_y = ship.get_position()
        orientation = ship.get_orientation()
        size = ship.get_size()

        # if the ship is on an occupied tile, fail
        for i in range(size):
            if (orientation == shipM.Orientation.HORIZONTAL and self.is_occupied(ship_x + i, ship_y)) or (orientation == shipM.Orientation.VERTICAL and self.is_occupied(ship_x, ship_y + i)):
                return False

        # if the ship is out of bounds, fail
        if (orientation == shipM.Orientation.HORIZONTAL and ship_x + size > Board.SIZE) or (orientation == shipM.Orientation.VERTICAL and ship_y + size > Board.SIZE):
            return False

        self.__ships.append(ship)
        return True

    def draw(self) -> str:
        board = [" ".join("[x]" if self.is_occupied(x, y) else "[ ]" for x in range(Board.SIZE)) for y in range(Board.SIZE)]
        print("\n".join(board))