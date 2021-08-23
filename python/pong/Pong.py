import pygame
from Paddle import Paddle
from Ball import Ball

pygame.init()

# Constants
BLACK = (0,0,0)
WHITE = (255,255,255)

# Open a window
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption('newt\'s pong!')

leftPaddle = Paddle(WHITE, 10, 100)
leftPaddle.rect.x = 20
leftPaddle.rect.y = 200

rightPaddle = Paddle(WHITE, 10, 100)
rightPaddle.rect.x = 670
rightPaddle.rect.y = 200

ball = Ball(WHITE, 20, 20)
ball.rect.x = 345
ball.rect.y = 195

# Populate a sprite list
spriteList = pygame.sprite.Group()
spriteList.add(leftPaddle)
spriteList.add(rightPaddle)
spriteList.add(ball)

# Game loop
running = True
clock = pygame.time.Clock()

# Scores
player1 = 0
player2 = 0

while running:
    # Main event loop
    for e in pygame.event.get():
        # If a user wants to quit, end the loop
        if e.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]: # Left, up
        leftPaddle.move(6)
    if keys[pygame.K_s]: # Left, down
        leftPaddle.move(-6)
    if keys[pygame.K_UP]: # Right, up
        rightPaddle.move(6)
    if keys[pygame.K_DOWN]: # Right, down
        rightPaddle.move(-6)

    # Logic
    spriteList.update()

    # Check if the ball is bouncing against any walls
    if ball.rect.x >= 690:
        player1 += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        player2 += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490 or ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions
    if pygame.sprite.collide_mask(ball, leftPaddle) or pygame.sprite.collide_mask(ball, rightPaddle):
        ball.bounce()

    # Drawing code
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    spriteList.draw(screen)

    # Display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(player1), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(player2), 1, WHITE)
    screen.blit(text, (420, 10))

    # Update screen
    pygame.display.flip()

    # Limit frames
    clock.tick(60)

# Quit the game
pygame.quit()