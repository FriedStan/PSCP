"""Sequence V"""


def sequence_05(count):
    """Do as <e>judge said"""
    while count > 0:
        for _ in range(7):
            print(count if count > 0 else " ", end=" ")
            count -= 1
        print()


sequence_05(int(input()))
