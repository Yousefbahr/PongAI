import pygame
from Game import *

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)
gray_white = (180, 180, 180)
red = (255 ,0 ,0)

# Set screen
pygame.init()
HEIGHT, WIDTH, SIZE = 35, 30, 20
screen = pygame.display.set_mode((HEIGHT * SIZE, WIDTH * SIZE))
FPS = 30
clock = pygame.time.Clock()
background = pygame.Surface((HEIGHT * SIZE, WIDTH * SIZE))
background.fill(black)
pygame.draw.line(background, gray_white, ((HEIGHT * SIZE) // 2, 0), ((HEIGHT * SIZE) // 2, WIDTH * SIZE), 5)

# Set game
player1 = Pong(body=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
player2 = Pong(body=[(HEIGHT - 1, 0), (HEIGHT - 1, 1), (HEIGHT - 1, 2), (HEIGHT - 1, 3), (HEIGHT - 1, 4)])
ball = (80, 20)

EXIT = False

while True:

    if EXIT:
        break

    clock.tick(FPS)
    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Down
    if keys[pygame.K_s]:
        player1.direction = (0, 1)
    # UP
    if keys[pygame.K_w]:
        player1.direction = (0, -1)
    # DOWN
    if keys[pygame.K_DOWN]:
        player2.direction = (0, 1)
    # UP
    if keys[pygame.K_UP]:
        player2.direction = (0, -1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EXIT = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                EXIT = True

    screen.blit(background, (0, 0))

    # move players
    player1.move(WIDTH)
    player2.move(WIDTH)

    # Collision
    if ball in player2.body:
        ball = (ball[0] - 20,  ball[1])

    # Move ball
    ball = (ball[0] + 7, ball[1])

    # Draw ball
    pygame.draw.circle(screen, red, ball, 10, 0)

    # Draw player1
    for i, position in enumerate(player1.body):
        pygame.draw.rect(screen, white, (position[0] * SIZE, position[1] * SIZE, SIZE, SIZE))
    # Draw player2
    for j, pos in enumerate(player2.body):
        pygame.draw.rect(screen, white, (pos[0] * SIZE, pos[1] * SIZE, SIZE, SIZE))

    print(player1)
    print(f"ball {ball}")

    pygame.display.flip()









