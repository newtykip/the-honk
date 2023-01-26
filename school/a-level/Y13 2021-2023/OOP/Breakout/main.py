import pygame
from pathlib import Path
from paddle import Paddle
from ball import Ball
from brick import Brick
from border import Border

# Colours
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

MOVEMENT_UNIT = 5
BRICK_WIDTH = 50

pygame.init()

# Prepare the display and set up the clock
dimensions = (800, 600)
screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
font = pygame.font.Font(str(Path(__file__).parent / 'Comfortaa-Bold.ttf'), 20)

pygame.display.set_caption('Breakout!')

# Game variables
playing = True
score = 0
lives = 3

# Sprites
spriteList = pygame.sprite.Group()

paddle = Paddle(100, 10, (350, 560), LIGHTBLUE, dimensions[0])
ball = Ball(10, 10, (150, 150), WHITE)
border = Border(dimensions[0], dimensions[1], (0, 0), DARKBLUE)

spriteList.add(paddle)
spriteList.add(ball)

# Bricks
bricks = pygame.sprite.Group()

for i in range(0, (dimensions[0] // BRICK_WIDTH)):
    brick = Brick(BRICK_WIDTH, 20, ((2 * i + 1) * BRICK_WIDTH, 100), WHITE)
    bricks.add(brick)

# Main loop
while playing:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False

    # Handle keypresses
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.moveLeft(MOVEMENT_UNIT)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(MOVEMENT_UNIT)

    # Game logic
    spriteList.update()
    bricks.update()

    if ball.rect.x >= (dimensions[0] - 10):
        ball.velocity[0] = -ball.velocity[0]
    elif ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.y >= (dimensions[1] - 10):
        ball.velocity[1] = -ball.velocity[1]
    elif ball.rect.y <= 40:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, border) and ball.rect.y > paddle.rect.y and ball.rect.x < (dimensions[0] - 10) and ball.rect.x > 0:
        lives -= 1
        # todo: reset ball

    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.bottom = ball.rect.top
        ball.bounce()

    collidedBrick = pygame.sprite.spritecollideany(ball, bricks)

    if collidedBrick:
        collidedBrick.kill()
        ball.velocity[1] = -ball.velocity[1]
        score += 1

    # Rendering
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))

    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))

    text = font.render(f'FPS: {clock.get_fps():.0f}' , 1, WHITE)
    screen.blit(text, (dimensions[0] - text.get_width() - 20, dimensions[1] - text.get_height() - 10))

    spriteList.draw(screen)
    bricks.draw(screen)

    # Update the screen and cap the FPS at 60 (todo: make refresh rate)
    pygame.display.flip()
    clock.tick(60)  