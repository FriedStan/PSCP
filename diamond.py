"""Daimond"""


def daimond_maker(size):
    """Make a daimond at order"""
    length = size // 2 * -1
    for row in range(size // 2):
        for col in range(length, size - 1):
            if row != abs(col):
                print(" ", end="")
            else:
                print("*", end="")
        print()
    print("*" * size)
    for row in range((size // 2) - 1, -1, -1):
        for col in range(length, size - 1):
            if row != abs(col):
                print(" ", end="")
            else:
                print("*", end="")
        print()


daimond_maker(int(input()))
