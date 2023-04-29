import math
import random

last_move = 0


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


def collision_point(ball, PADDLE_HEIGHT, paddle):
    """
    return location of collision either: top ,bottom , or center
    and location point (the point where the ball touched the paddle ,where 0 is the center of the paddle)
    """
    location_point = (ball[1] - (PADDLE_HEIGHT / 2 + paddle.top)) / (PADDLE_HEIGHT / 2)
    if location_point <= -0.2:
        return "top", location_point
    elif -0.2 <= location_point < 0.2:
        return "center", location_point
    else:
        return "bottom", location_point


def get_avg_point(location, history):
    """
    return avg number of points where ball touched the paddle on that
    'location' --> either 'top', 'bottom', or 'center'
    """
    return sum(history[location]) / (len(history[location]) + 1)


def predict(history):
    """
    return location of impact based on history
    """
    total = len(history["top"]) + len(history["bottom"]) + len(history["center"]) + 1
    top = (len(history["top"]) / total) * 100
    center = (len(history["center"]) / total) * 100
    bottom = (len(history["bottom"]) / total) * 100
    return random.choices(["top","center", "bottom"], weights=(top, center,bottom), k=1)[0]


def ball_collided_paddle(ball, RADIUS, paddle):
    """
    return True if ball collided with paddle
    else return false
    """
    return paddle.top - RADIUS <= ball[1] <= paddle.bottom + RADIUS \
        and paddle.left - RADIUS <= ball[0] <= paddle.right + RADIUS


def collided(paddle1, paddle2, ball, ball_speed, PADDLE_HEIGHT, MAXANGLE, HEIGHT, RADIUS):
    """
    Check if ball colided with either paddles, if True return the speed of ball,
    else return None
    paddle is a Rect object
    """
    # Paddle1 is user's paddle
    if ball_collided_paddle(ball, RADIUS, paddle1):
        return get_speed(paddle1, ball, ball_speed, PADDLE_HEIGHT, MAXANGLE, HEIGHT)

    # Paddle2 is ai's paddle
    if ball_collided_paddle(ball, RADIUS, paddle2):
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
    # if paddle.top - 10 <= ball[1] <= paddle.top + 10 or paddle.bottom - 10 <= ball[1] <= paddle.bottom + 10  :
    #     MAXANGLE = math.pi / 3
    #     ball_speed = 0.7

    normal = (ball[1] - (PADDLE_HEIGHT / 2 + paddle.top)) / (PADDLE_HEIGHT / 2)
    bounce_angle = normal * MAXANGLE
    vx = ball_speed * math.cos(bounce_angle)
    vy = ball_speed * math.sin(bounce_angle)

    if paddle.right == HEIGHT:
        vx = -vx

    return vx, vy


def move(paddle, paddle_height, step, ball ,time, vx, vy, width, height, history, RADIUS, MAXANGLE, ball_speed):
    """
    return movement of AI's paddle
     """

    x, y = calculate(ball, time, vx, vy, height=height, width=width, history=history,
                     paddle=paddle,RADIUS=RADIUS, max_angle=MAXANGLE, ball_speed=ball_speed)
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


def calculate(ball, time, vx, vy, height, width, history, paddle, RADIUS, max_angle, ball_speed):
    """
    return future coordinate of where the ball is going to be near the paddle
    calculate a round trip of the ball from AI's paddle
    predict how user will play
    """
    global last_move
    ball = list(ball)
    # Track ball's trajectory to know its impact's location on AI's paddle
    while True:
        if border_collided(ball, width):
            vy = -vy

        if (height - 20 <= ball[0] <= height or (ball[0] > height)) or ball[0] <= 20:
            break

        posx = vx * time
        posy = vy * time

        ball[0] += round(posx)
        ball[1] += round(posy)
    # towards AI's paddle
    if vx >= 0:
        return ball
    # Track ball's trajectory to know its impact's location on user's paddle
    else:
        if ball_collided_paddle(ball, RADIUS, paddle):
            while True:
                if border_collided(ball, width):
                    vy = -vy

                posx = vx * time
                posy = vy * time
                if ball[0] <= 20:
                    break

                ball[0] += round(posx)
                ball[1] += round(posy)

            # Predict user's impact location, and track ball's trajectory as it returns to AI's paddle
            location = predict(history)
            point = get_avg_point(location, history)
            bounce_angle = point * max_angle
            vx = ball_speed * math.cos(bounce_angle)
            vy = ball_speed * math.sin(bounce_angle)
            while True:
                if border_collided(ball, width):
                    vy = -vy

                posx = vx * time
                posy = vy * time
                if height - 20 <= ball[0] <= height or (ball[0] > height):
                    last_move = ball
                    return ball

                ball[0] += round(posx)
                ball[1] += round(posy)
        else:
            return last_move






