import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move(self, px):
        self.rect.y -= px
        # Ensure that you are still on the screen
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 400:
            self.rect.y = 400