from pygame.sprite import Sprite
from pygame.draw import rect as drawRect
from pygame import Surface

BLACK = (0, 0, 0)

class Element(Sprite):
    def __init__(self, width, height, startPosition, colour, fill = True):
        super().__init__()

        self.image = Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        drawRect(self.image, colour, [0, 0, width, height], 0 if fill else 2)
        self.rect = self.image.get_rect()

        self.__startPosition = startPosition
        self.reset()

    def reset(self):
        self.rect.x = self.__startPosition[0]
        self.rect.y = self.__startPosition[1]