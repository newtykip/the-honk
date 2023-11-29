import pygame
from element import Element

BLACK = (0, 0, 0)

class Brick(Element):
    def __init__(self, width, height, startPosition, colour):
        super().__init__(width, height, startPosition, colour)