import math
import random


def border_collided(ball, width):
    """
    return True if ball collided with top or bottom borders
    else return False
    """
    return ball[1] <= 28 or ball[1] >= width - 25


def ai_scored(ball, HEIGHT):
    """
    Update Scores
    """
    return ball[0] > HEIGHT + 10


def player_scored(ball):
    """
    Update Scores
    """
    return ball[0] < -10


def collided(paddle1, paddle2, ball, ball_speed, PADDLE_HEIGHT, MAXANGLE, HEIGHT, RADIUS):
    """
    Check if ball colided with either paddles, if True return the speed of ball,
    else return None
    paddle is a Rect object
    """
    # Paddle1 is user's paddle
    if paddle1.top - RADIUS <= ball[1] <= paddle1.bottom + RADIUS and paddle1.left - RADIUS <= ball[0] <= paddle1.right + RADIUS:
        return get_speed(paddle1, ball, ball_speed, PADDLE_HEIGHT, MAXANGLE, HEIGHT)

    # Paddle2 is ai's paddle
    if paddle2.top - RADIUS <= ball[1] <= paddle2.bottom + RADIUS and paddle2.left - RADIUS <= ball[0] <= paddle2.right + RADIUS:
        return get_speed(paddle2, ball, ball_speed, PADDLE_HEIGHT, MAXANGLE, HEIGHT)

    return None


def get_speed(paddle, ball, ball_speed, PADDLE_HEIGHT, MAXANGLE, HEIGHT):
    """
    Return ball speed in x-axis and y-axis if ball collided with paddle,
    else return None
    paddle, Rect object
    ball, tuple, representing coordinate position of the ball
    ball_speed, int, representing speed of the ball
    PADDLE_HEIGHT, int, height of the paddle
    RADIUS, int, radius of the ball
    MAXANGLE, int, maximum angle by which ball will bounce
    """
    if paddle.top - 10 <= ball[1] <= paddle.top + 10 or paddle.bottom - 10 <= ball[1] <= paddle.bottom + 10  :
        MAXANGLE = math.pi / 3
        ball_speed = 0.7

    normal = (ball[1] - (PADDLE_HEIGHT / 2 + paddle.top)) / (PADDLE_HEIGHT / 2)
    bounce_angle = normal * MAXANGLE
    vx = ball_speed * math.cos(bounce_angle)
    vy = ball_speed * math.sin(bounce_angle)

    if paddle.right == HEIGHT:
        vx = -vx

    return vx, vy


def move(paddle, paddle_height, step, ball ,time, vx, vy, width, height):
    # Don't calculate trajectory when ball going other way
    if vx <= 0:
        return 0

    x, y = calculate(ball, time, vx, vy, height=height, width=width)
    x, y = int(x), int(y)

    if paddle.top <= ball[1] <= paddle.bottom and width - 50 <= ball[0] <= width - 20:
        movement = random.choice(["top", "bottom", "center"])

        if movement == "top":
            if y > paddle.top + (paddle_height / 2) - 10:
                return step
            else:
                return 0

        if movement == "bottom":
            if y < paddle.bottom + (paddle_height / 2) + 10:
                return -step
            else:
                return 0

        if movement == "center":
            if paddle.top + (paddle_height / 2) - 10 <= y <= paddle.top + (paddle_height / 2) + 10:
                return 0
            if y < paddle.top + (paddle_height / 2):
                return -step
            elif y > paddle.top + (paddle_height / 2):
                return step

    if paddle.top <= y <= paddle.bottom:
        return 0

    elif paddle.top > y:
        return -step

    elif paddle.top < y:
        return step


def calculate(ball, time, vx, vy, height, width):
    """
    return future coordinate of where the ball is going to be near the paddle
    """
    ball = list(ball)
    while True:
        if border_collided(ball, width):
            vy = -vy

        posx = vx * time
        posy = vy * time
        if (height - 10 <= ball[0] <= height and posx >= 0) or (ball[0] > height):
            return ball

        ball[0] += round(posx)
        ball[1] += round(posy)
