"""Make arrow for gov"""


def arrow_maker(length, width):
    """Making arrow"""
    for i in range(width, 0, -1):
        print(" " * i + "*" * length)
    print("*" * length)
    for i in range(width):
        print(" " * (i + 1) + "*" * length)


arrow_maker(int(input()), int(int(input()) / 2))
