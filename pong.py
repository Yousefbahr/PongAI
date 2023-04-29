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
font = pygame.font.Font('freesansbold.ttf', 30)
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
BALL_SPEED = 0.6
ball = (HEIGHT // 2, WIDTH // 2)
RADIUS = 10
EXIT = False
MAXANGLE = (math.pi / 3)
vx = 0.2
vy = -0.2
step = 5
score_ai = 0
score_player = 0
# Track history of the ball's collision location on user's paddle
history = {'top': [],
           "center": [],
           "bottom": []}

while True:
    if EXIT:
        break

    clock.tick(FPS)
    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Down
    if keys[pygame.K_s] and paddle1.bottom < WIDTH:
        paddle1.move_ip(0, step)

    # UP
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0, -step)

    # DOWN
    if keys[pygame.K_DOWN] and paddle2.bottom < WIDTH:
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

    # Update scores
    score_player += player_scored(ball)
    score_ai += ai_scored(ball, HEIGHT)

    # Display Scores
    score1 = font.render(f"{score_ai}", True, white)
    score2 = font.render(f"{score_player}", True, white)
    score_rect1 = score1.get_rect()
    score_rect2 = score2.get_rect()
    score_rect1.center = ((HEIGHT // 2) - 50, 20)
    score_rect2.center = ((HEIGHT // 2) + 50, 20)
    screen.blit(score1, score_rect1)
    screen.blit(score2, score_rect2)

    # Track history of the collision's location of the user's paddle
    if ball_collided_paddle(ball, RADIUS, paddle1):
        location, point = collision_point(ball, PADDLE_HEIGHT, paddle1)
        history[location].append(point)

    # Get speed of ball if collided
    try:
        vx, vy = collided(paddle1, paddle2, ball, BALL_SPEED, PADDLE_HEIGHT, MAXANGLE, HEIGHT, RADIUS)

    # Ball didn't collide
    except TypeError:
        pass

    # Ball doesn't cross top and bottom borders
    if border_collided(ball, WIDTH):
        vy = -vy

    ai_move = move(paddle2, PADDLE_HEIGHT, step, ball, millisec_per_frame, vx, vy, width=WIDTH,
                   height=HEIGHT, history=history,RADIUS=RADIUS, MAXANGLE=MAXANGLE, ball_speed=BALL_SPEED)

    # Not moving beyond boundaries
    if ai_move > 0 and paddle2.bottom < WIDTH: # DOWN
        paddle2.move_ip(0, ai_move)
    elif ai_move < 0 and paddle2.top > 0: # UP
        paddle2.move_ip(0, ai_move)

    # if Ball out of left or right borders
    if player_scored(ball) or ai_scored(ball, HEIGHT):
        ball = (HEIGHT // 2, random.randint(70, WIDTH))
        vx = 0.2 * random.choice([1, -1])
        vy = -0.2 * random.choice([1, -1])

    ball = round(ball[0] + (vx * millisec_per_frame)), round(ball[1] + (vy * millisec_per_frame))

    # Draw ball
    pygame.draw.circle(screen, red, (ball[0], ball[1]), RADIUS, 0)

    # Draw paddles
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)

    pygame.display.flip()



