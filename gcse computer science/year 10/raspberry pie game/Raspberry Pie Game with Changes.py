import math, random, pygame, sys

# Game class
class Game():
    def __init__(self):
        self.score = 0
        self.raspberryCount = 0

# Turret class
class Turret(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # extend the pygame Sprite class
        self.image = pygame.image.load('turret.png')
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 630

    # Method that enables the turret to move
    def move(self, direction):
        if direction == 'left' and self.rect.x > 5:
            self.rect.x -= 5
        if direction == 'right' and self.rect.x < (480 - self.rect.width):
            self.rect.x += 5

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, turret):
        pygame.sprite.Sprite.__init__(self) # extend the pygame Sprite class
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.rect.x = turret.rect.x + (turret.rect.width / 2) - (self.rect.width / 2)
        self.rect.y = turret.rect.y - turret.rect.height

    # Method that moves bullets up the screen
    def updatePosition(self):
        if self.rect.y > 0 - self.rect.height: # ensures that the bullet is on the screen
            self.rect.y -= 5
        else:
            self.kill() # remove the bullet when it goes off of the screen

# Fruit class
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Determine the type of fruit it will be
        self.genus = random.randint(1, 3)

        if self.genus == 1: imageFile = 'raspberry'
        elif self.genus == 2: imageFile = 'strawberry'
        elif self.genus == 3: imageFile = 'cherry'

        self.image = pygame.image.load('{0}.png'.format(imageFile)) # load the type of fruit
        self.image = pygame.transform.rotate(self.image, -15 + random.randint(0, 20)) # rotate the fruit

        self.rect = self.image.get_rect()
        self.rect.y = 0 - self.rect.height
        self.rect.x = random.randint(2, 44) * 10

    # Method that moves fruit down the screen
    def updatePosition(self, game):
        if self.rect.y < 640: # ensures that the fruit is on the screen
            self.rect.y += 3
        else:
            if self.genus == 1: # if the fruit was a raspberry
                game.score += 10 # add 10 points
                game.raspberryCount += 1 # increase raspberry count
            else: # otherwise
                game.score -= 50 # remove 50 points
            self.kill() # remove the fruit

    # Method to update score and remove fruit when shot
    def shot(self, game, bullet):
        if self.genus == 1:
            game.score -= 50
            game.raspberryCount += 1
        else:
            game.score += 10
        self.kill()
        bullet.kill()

# Bullet timeout function
keyTimeout = {}
def keyPressed(keys, key, timeout):
    if keys[key] == False:
        return False

    currentTime = pygame.time.get_ticks()

    if key in keyTimeout and keyTimeout[key] > currentTime:
        return False

    keyTimeout[key] = currentTime + timeout
    return True

# Initialise the game
pygame.init()
pygame.key.set_repeat(1, 20)
scoreFont = pygame.font.Font(None, 17) # set the score font
statusFont = pygame.font.Font(None, 17) # set the status font
black = (0, 0, 0) # rgb for black
screen = pygame.display.set_mode([480, 640]) # set the size of the window
pygame.display.set_caption('Raspberry Pie') # set the title of the window

# Create initial object instances
game = Game()
turret = Turret()
fruits = pygame.sprite.Group()
bullets = pygame.sprite.Group()

sprites = pygame.sprite.Group()
sprites.add(turret)

# Initialize game over flag and timer
endGame = False
clock = pygame.time.Clock()
tock = 0

# Game loop
while endGame == False:
    clock.tick(30)
    tock += 1
    screen.fill(black)

    # Process events
    for event in pygame.event.get():
        # Handle exiting
        if event.type == pygame.QUIT:
            sys.exit()

    # Handle key presses
    keys = pygame.key.get_pressed()

    # If the key was the left arrow
    if keys[pygame.K_LEFT]:
        turret.move('left')
    # If the key was the right arrow
    if keys[pygame.K_RIGHT]:
        turret.move('right')
    # If the key was the space key
    if keyPressed(keys, pygame.K_SPACE, 1000):
        bullet = Bullet(turret)
        bullets.add(bullet)
    # If the key was the escape key
    if keys[pygame.K_ESCAPE]:
        sys.exit()

    # Move objects
    for bullet in bullets:
        bullet.updatePosition()
    for fruit in fruits:
        fruit.updatePosition(game)

    # Add new fruit if two seconds has elapsed
    if tock > 60:
        if len(fruits) < 10: # cap the amount of fruits to be less than 10
            fruit = Fruit()
            fruits.add(fruit)
        tock = 0 # reset counter

    # Check for collisions
    collisions = pygame.sprite.groupcollide(fruits, bullets, False, True)

    if collisions:
        for fruit in collisions:
            fruit.shot(game, collisions[fruit][0])

    # Update player score
    scoreText = scoreFont.render('Score: {0}'.format(str(game.score)), True, (255, 255, 255), (0, 0, 0))
    screen.blit(scoreText, (0, 620)) # put the score onto the screen at 0, 620

    statusText = statusFont.render('Raspberries: {0}'.format(str(10 - game.raspberryCount)), True, (255, 210, 210), (0, 0, 0))
    screen.blit(statusText, (0, 10))

    # Update the screen and check for game over
    sprites.draw(screen)
    bullets.draw(screen)
    fruits.draw(screen)
    pygame.display.flip()

    if game.raspberryCount >= 10:
        endGame = True


# Game over: display the player's final score
scoreBadge = pygame.image.load('scoreframe.png')
scoreBadge.convert_alpha()
screen.blit(scoreBadge, (90, 250))

scoreFont = pygame.font.Font(None, 52)
statusText = scoreFont.render('Your Score: {0}'.format(str(game.score)), True, (0, 0, 0), (231, 230, 33))
screen.blit(statusText, (105, 300))

pygame.display.flip()

# Wait for the player to close the game window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
