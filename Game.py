import math


def collided(paddle1, paddle2, ball, ball_speed, PADDLE_HEIGHT, MAXANGLE, HEIGHT, RADIUS):
    """
    Check if ball colided with either paddles, if True return the speed of ball,
    else return None
    paddle is a Rect object
    """
    if paddle1.top - RADIUS <= ball[1] <= paddle1.bottom + RADIUS and paddle1.left - RADIUS <= ball[0] <= paddle1.right + RADIUS:
        return get_speed(paddle1, ball, ball_speed, PADDLE_HEIGHT, MAXANGLE, HEIGHT)

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

    normalized = (ball[1] - (PADDLE_HEIGHT / 2 + paddle.top) ) / (PADDLE_HEIGHT / 2)
    bounce_angle = normalized * MAXANGLE
    vx = ball_speed * math.cos(bounce_angle)
    vy = ball_speed * math.sin(bounce_angle)

    if paddle.right == HEIGHT:
        vx = -vx

    return vx, vy


