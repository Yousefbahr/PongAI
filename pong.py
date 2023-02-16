import random
import pygame
from Game import *
import math

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)
gray_white = (180, 180, 180)
red = (255 ,0 ,0)
blue = (0, 0, 255)
green = (0, 180, 0)

# Set screen
pygame.init()
WIDTH, HEIGHT = 400, 700
screen = pygame.display.set_mode((HEIGHT, WIDTH))
FPS = 40
millisec_per_frame = (1 / (FPS / 1000))
clock = pygame.time.Clock()
background = pygame.Surface((HEIGHT, WIDTH))
background.fill(black)
pygame.draw.line(background, gray_white, (HEIGHT // 2, 0), (HEIGHT // 2, WIDTH), 5)

# Set game
PADDLE_HEIGHT = 70
paddle1 = pygame.Rect(0, 0, 10, PADDLE_HEIGHT)
paddle2 = pygame.Rect(HEIGHT - 10, 0, 10, PADDLE_HEIGHT)
# speed in pixels/ milliseconds
ball_speed = 0.5
ball = (HEIGHT // 2, WIDTH // 2)
RADIUS = 10
EXIT = False
MAXANGLE = (math.pi / 2)
vx = 0.2
vy = -0.2
step = 7

while True:
    move = (0, 0)
    if EXIT:
        break

    clock.tick(FPS)
    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Down
    if keys[pygame.K_s] and paddle1.bottom < 400:
        paddle1.move_ip(0, step)
    # UP
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0, -step)

    # right
    if keys[pygame.K_l]:
        move = (5, 0)

    # left
    if keys[pygame.K_j]:
        move = (-5, 0)

    # up
    if keys[pygame.K_i]:
        move = (0, -5)
    # down
    if keys[pygame.K_k]:
        move = (0, 5)

    # DOWN
    if keys[pygame.K_DOWN] and paddle2.bottom < 400:
        paddle2.move_ip(0, step)

    # UP
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.move_ip(0, -step)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EXIT = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                EXIT = True

    screen.blit(background, (0, 0))

    #ball = (ball[0] + move[0], ball[1] + move[1])

    # Get speed of ball if coliided
    try:
        vx, vy = collided(paddle1, paddle2, ball, ball_speed, PADDLE_HEIGHT, MAXANGLE, HEIGHT, RADIUS)

    # Ball didn't collide
    except TypeError:
        pass

    # Ball doesn't cross borders
    if ball[1] <= 13 or ball[1] >= 385:
        vy = -vy

    # if Ball out of borders
    if ball[0] > HEIGHT + 10 or ball[0] < -10:
        ball = (HEIGHT // 2, WIDTH // 2)
        vx = 0.2
        vy = -0.2

    ball = ball[0] + (vx * millisec_per_frame), ball[1] + (vy * millisec_per_frame)

    # Draw ball
    pygame.draw.circle(screen, red, (ball[0], ball[1]), RADIUS, 0)

    # Draw paddles
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)

    pygame.display.flip()









