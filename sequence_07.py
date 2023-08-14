"""Sequence VII"""


def sequence_07(count):
    """Do as <e>judge said"""
    for i in range(1, count + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(count, 1, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()

sequence_07(int(input()))
