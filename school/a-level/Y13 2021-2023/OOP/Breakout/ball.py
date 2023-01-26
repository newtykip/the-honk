from random import randint
from element import Element

BLACK = (0, 0, 0)

class Ball(Element):
    def __init__(self, width, height, startPosition, colour):
        super().__init__(width, height, startPosition, colour)
        self.reset()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity = [ randint(-6, 6), -self.velocity[1]]

    def reset(self):
        Element.reset(self)
        self.velocity = [randint(4, 6), randint(-6, 6)]