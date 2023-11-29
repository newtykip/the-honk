from __future__ import annotations
from structs.player import Player
from structs.board import Board
from structs.ship import Ship, ShipType, Orientation

p1, p2 = Player("me"), Player("you")
game = Board(p1, p2)

print(game.add_ship(Ship(ShipType.SUBMARINE, (0, 0), Orientation.HORIZONTAL, p1)))
print(game.add_ship(Ship(ShipType.SUBMARINE, (1, 1), Orientation.VERTICAL, p1)))
game.draw()