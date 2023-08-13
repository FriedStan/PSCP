"""Steel Balls Run"""


def reflector(ball_start):
    """Calculate How many times that ball bounced"""
    ball_end = ball_start * 100
    count = 0
    while True:
        ball_end *= 3/5
        if ball_end < 1:
            break
        count += 1
    return count


print(reflector(float(input())))
