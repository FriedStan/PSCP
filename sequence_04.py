"""Sequence IV"""


def sequence_04(count):
    """Do as <e>judge said"""
    adder = 0
    for _ in range(1, count + 1):
        for j in range(1, count + 1):
            print(j + adder, end=" ")
        print()
        adder += count


sequence_04(int(input()))
