from element import Element

BLACK = (0, 0, 0)

class Paddle(Element):
    def __init__(self, width, height, startPosition, colour, screenWidth):
        super().__init__(width, height, startPosition, colour)
        self.__screenWidth = screenWidth - width

    def moveLeft(self, px):
        self.rect.x -= px

        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, px):
        self.rect.x += px

        if self.rect.x > self.__screenWidth:
            self.rect.x = self.__screenWidth