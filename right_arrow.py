"""Right Arrow"""


def right_arrower(width, height):
    """Make a right arrow"""
    for i in range(0, int(height / 2)):
        print(" " * i + "*" * width)
    for i in range(int(height / 2), -1, -1):
        print(" " * i + "*" * width)


right_arrower(int(input()), int(input()))
