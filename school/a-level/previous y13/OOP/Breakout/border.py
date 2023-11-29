from element import Element
from pygame import Color

class Border(Element):
    def __init__(self, width, height, startPosition, colour):
        super().__init__(width, height, startPosition, colour, False)