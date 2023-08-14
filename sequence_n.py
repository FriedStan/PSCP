"""Sequence N"""


def sequence_n(size):
    """Making N"""
    for row in range(size):
        for col in range(size):
            if col in (row, 0, size - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()


sequence_n(int(input()))
