"""Sequence VI"""


def sequence_06(count):
    """Do as <e>judge said"""
    for i in range(1, count + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


sequence_06(int(input()))
