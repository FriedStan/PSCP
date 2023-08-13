"""Sequence XXX"""


def sequencer_30(size, amount):
    """Do as <e>judge says"""
    length = (amount * size) + amount - 1
    for _ in range(size):
        for i in range(length):
            if (i + 1) % (size + 1) == 0:
                print(" ", end="")
            else:
                print("*", end="")
        print()
    for row in range(size):
        for col in range(size):
            if row == col or col in (0, size - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()


sequencer_30(int(input()), int(input()))
