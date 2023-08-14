"""Sequence I"""


def sequence_01(count):
    """Do as <e>judge said"""
    for _ in range(count):
        for i in range(1, count):
            print(i, end=" ")
        print(count)


sequence_01(int(input()))
