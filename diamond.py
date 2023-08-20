"""Daimond"""


def daimond_maker(size):
    """Make a daimond at order"""
    length = size // 2 * -1
    for row in range(length, (size // 2) + 1):
        for col in range(length, (size // 2) + 1):
            if row == 0:
                print("*", end="")
            elif size // 2 in (abs(row + col), abs(row - col)):
                print("*", end="")
            else:
                print(" ", end="")
        print()


daimond_maker(int(input()))
