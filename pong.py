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
#HEIGHT, WIDTH, SIZE = 35, 30, 20
HEIGHT, WIDTH = 500, 400
screen = pygame.display.set_mode((HEIGHT, WIDTH))
FPS = 40
clock = pygame.time.Clock()
background = pygame.Surface((HEIGHT, WIDTH))
background.fill(black)
pygame.draw.line(background, gray_white, ((HEIGHT) // 2, 0), ((HEIGHT) // 2, WIDTH), 5)

# Set game
#player1 = Pong(body=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
# player2 = Pong(body=[(HEIGHT - 10, 0), (HEIGHT - 10, 1), (HEIGHT - 10, 2), (HEIGHT - 10, 3), (HEIGHT - 10, 4)])
PADDLE_HEIGHT = 70
player1 = pygame.Rect(0, 0, 10, PADDLE_HEIGHT)
player2 = pygame.Rect(HEIGHT - 10, 0, 10, PADDLE_HEIGHT)


ball_speed = 0.3 # pixels/ milliseconds
ball = (50, 50)
RADIUS = 10
EXIT = False
MAXANGLE = (math.pi/ 2) # 75 degrees

ballvx = 0
ballvy = 0
step = 1
ball_rect = pygame.Rect(0, 0, 20, 20)
x = 0
while True:
    move = (0, 0)
    if EXIT:
        break

    clock.tick(FPS)
    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Down
    if keys[pygame.K_s]:
        #player1.direction = (0, 1)
        player1.move_ip(0, 5)
    # UP
    if keys[pygame.K_w]:
        #player1.direction = (0, -1)
        player1.move_ip(0, -5)

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
    if keys[pygame.K_DOWN]:
        # player2.direction = (0, 1)
        player2.move_ip(0, 5)

    # UP
    if keys[pygame.K_UP]:
        player2.move_ip(0, -5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EXIT = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                EXIT = True

    screen.blit(background, (0, 0))

    # move players
    #player1.move(WIDTH)
    #player2.move(WIDTH)

    # bounce_angle = normalized_intersectY * MAXANGLE
    # ballvx = ball[0] * math.cos(bounce_angle)
    # ballvy = ball[1] * math.sin(bounce_angle)
    # print(ballvy)
    # print(ballvx)
    # print(ball_intersectY)
    # Move ball
    ball = (ball[0] + move[0], ball[1] + move[1])

    # ball = ball[0] + ballvx, ball[1] +  ballvy
    # if ball[1] >= 29 or ball[1] <= 1:
    #    ball= -ball[0] , -ball[1]

    # ball = (ball[0] + step, ball[1])

    # # Detect collision
    if player1.top - RADIUS <= ball[1] <= player1.bottom + RADIUS and player1.left - RADIUS <= ball[0] <= player1.right + RADIUS:
        if player1.top - 10 <= ball[1] <= player1.top + 10:
            MAXANGLE = math.pi / 3

        intersecty = ((PADDLE_HEIGHT / 2 + player1.top) + (PADDLE_HEIGHT / 2)) - ball[1]
        normalized = (ball[1] - (PADDLE_HEIGHT / 2 + player1.top) ) / (PADDLE_HEIGHT / 2)
        bounce_angle = normalized * MAXANGLE
        ballvx = ball_speed * math.cos(bounce_angle)
        ballvy = ball_speed * math.sin(bounce_angle)
        print(ballvx, ballvy)

    if player2.top - RADIUS <= ball[1] <= player2.bottom + RADIUS and player2.left - RADIUS <= ball[0] <= player2.right + RADIUS:
        if player2.top - 10 <= ball[1] <= player2.top + 10:
            MAXANGLE = math.pi / 3

        intersecty = ((PADDLE_HEIGHT / 2 + player2.top) + (PADDLE_HEIGHT / 2)) - ball[1]
        normalized = (ball[1] - (PADDLE_HEIGHT / 2 + player2.top)) / (PADDLE_HEIGHT / 2)
        bounce_angle = normalized * MAXANGLE
        ballvx = -ball_speed * math.cos(bounce_angle)
        ballvy = ball_speed * math.sin(bounce_angle)
        print(ballvx, ballvy)


    # if ball[0] == 1 and (ball[1] in [y for x, y in player1.body] or ball[1] == player1.body[-1][1] + 1):
    #     intersecty = (player1.body[len(player1.body) // 2][1] + (PADDLE_HEIGHT / 2)) - ball[1]
    #     normalized_y = intersecty / (PADDLE_HEIGHT / 2)
    #     bounce_angle = normalized_y * MAXANGLE
    #     ballvx = math.cos(bounce_angle)
    #     ballvy = math.sin(bounce_angle)
    #     # ball_vx = ba
    #     # ball = (ball[0] + 1, ball[1])
    #     # step = ball[1] - ball[1] / len(player1.body)
    #     step = 0.5

    # if ball[0] == HEIGHT - 1 and (ball[1] in [y for x, y in player2.body] or ball[1] == player2.body[-1][1] + 1):
    #     # ball = (ball[0] - 1, ball[1])
    #     # print("true")
    #     step = -0.5
    #     # step = - (ball[1] - ball[1] / len(player1.body))
    time = (1 / (FPS / 1000))
    ball = ball[0] + (ballvx * time), ball[1] + (ballvy * time)
    print(ball)
    # ball = ball[0] + (ballvx * (1 / (FPS / 1000))), ball[1] + (ballvy * (1 / (FPS / 1000)))
    x += 1
    if x % 30 == 0:
        ballvx = 0
        ballvy = 0
    #pygame.draw.rect(screen, white, ball_rect)
    # Draw ball
    pygame.draw.circle(screen, red, (ball[0], ball[1]), RADIUS, 0)

    # Draw player1
    # for position in player1.body:
    #     pygame.draw.rect(screen, white, (position[0], position[1], RADIUS, PADDLE_HEIGHT))
    pygame.draw.rect(screen, white, player1)
    pygame.draw.rect(screen, white, player2)

    # Draw player2
    # for pos in player2.body:
    #     pygame.draw.rect(screen, white, (pos[0] , pos[1], RADIUS, PADDLE_HEIGHT))

    #print(player1.x, player1.y)
    #print(player1.left, player1.right, player1.top, player1.bottom)
    # print(f"ball {ball}")
    # print(f"player2 {player2}")

    pygame.display.flip()









