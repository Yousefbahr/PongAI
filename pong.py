import pygame
from Game import *

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)
gray_white = (180, 180, 180)
red = (255 ,0 ,0)
blue = (0, 0, 255)
green = (0, 180, 0)

# Set screen
pygame.init()
HEIGHT, WIDTH, SIZE = 35, 30, 20
screen = pygame.display.set_mode((HEIGHT * SIZE, WIDTH * SIZE))
FPS = 15
clock = pygame.time.Clock()
background = pygame.Surface((HEIGHT * SIZE, WIDTH * SIZE))
background.fill(black)
pygame.draw.line(background, gray_white, ((HEIGHT * SIZE) // 2, 0), ((HEIGHT * SIZE) // 2, WIDTH * SIZE), 5)

# Set game
player1 = Pong(body=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
player2 = Pong(body=[(HEIGHT - 0.5, 0), (HEIGHT - 0.5, 1), (HEIGHT - 0.5, 2), (HEIGHT - 0.5, 3), (HEIGHT - 0.5, 4)])
ball = (10, 10)
RADIUS = 10
EXIT = False

while True:
    move = (0, 0)
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

    # right
    if keys[pygame.K_l]:
        move = (1, 0)

    # left
    if keys[pygame.K_j]:
        move = (-1, 0)

    # up
    if keys[pygame.K_i]:
        move = (0, -1)
    # down
    if keys[pygame.K_k]:
        move = (0, 1)


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


    # Move ball
    ball = (ball[0] + move[0], ball[1] + move[1])
    #ball = (ball[0] + 1, ball[1])


    # Detect collision
    if ball[0] == 1 and (ball[1] in [y for x, y in player1.body] or ball[1] == player1.body[-1][1] + 1):
        #ball = (ball[0] + 1, ball[1])
        print("True")

    if ball[0] == 34 and (ball[1] in [y for x, y in player2.body] or ball[1] == player2.body[-1][1] + 1):
        #ball = (ball[0] - 1, ball[1])
        print("True")



    # Draw ball
    pygame.draw.circle(screen, red, (ball[0] * SIZE, ball[1] * SIZE), 10, 0)

    # Draw player1
    for i, position in enumerate(player1.body):
        pygame.draw.rect(screen, white, (position[0] * SIZE, position[1] * SIZE, 10, SIZE))

    # Draw player2
    for j, pos in enumerate(player2.body):
        pygame.draw.rect(screen, white, (pos[0] * SIZE, pos[1] * SIZE, RADIUS, 20))

    print(player1)
    print(f"ball {ball}")
    #print(f"player2 {player2}")

    pygame.display.flip()









