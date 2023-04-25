
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
BALL_SPEED = 0.8
ball = (HEIGHT // 2, WIDTH // 2)
RADIUS = 10
EXIT = False
MAXANGLE = (math.pi / 3)
vx = 0.2
vy = -0.2
step = 5

while True:
    moveb = (0, 0)
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
        moveb = (5, 0)

    # left
    if keys[pygame.K_j]:
        moveb = (-5, 0)

    # up
    if keys[pygame.K_i]:
        moveb = (0, -5)
    # down
    if keys[pygame.K_k]:
        moveb = (0, 5)

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

    # ball = (ball[0] + moveb[0], ball[1] + moveb[1])



    # Get speed of ball if coliided
    try:
        vx, vy = collided(paddle1, paddle2, ball, BALL_SPEED, PADDLE_HEIGHT, MAXANGLE, HEIGHT, RADIUS)


    # Ball didn't collide
    except TypeError:
        pass


    ai_move = move(paddle2, PADDLE_HEIGHT, step, ball, millisec_per_frame, vx, vy, HEIGHT)

    # Not moving beyond boundaries
    if ai_move > 0 and paddle2.bottom < 400: # DOWN
        paddle2.move_ip(0, ai_move)
    elif ai_move < 0 and paddle2.top > 0: # UP
        paddle2.move_ip(0, ai_move)

    # print(ai_move)
    # print("paddle2 top", paddle2.top)
    # print("paddle1 top", paddle1.top)
    # print("paddle2 bottom", paddle2.bottom)
    # print("paddle1 bottom",paddle2.bottom)
    print(ball)



    # Ball doesn't cross top and bottom borders
    if border_collided(ball, WIDTH):
        vy = -vy



    # if Ball out of left or right borders
    if ball[0] > HEIGHT + 10 or ball[0] < -10:
        ball = (HEIGHT // 2, WIDTH // 2)
        vx = 0.2
        vy = -0.2

    ball = round(ball[0] + (vx * millisec_per_frame)), round(ball[1] + (vy * millisec_per_frame))

    #print("vx",vx)
    #print("vy", vy)
    # Draw ball
    pygame.draw.circle(screen, red, (ball[0], ball[1]), RADIUS, 0)

    # Draw paddles
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)

    pygame.display.flip()









