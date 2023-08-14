"""Sequence II"""


def sequence_02(count):
    """Do as <e>judge said"""
    pattern = 1
    adder = 0
    for _ in range(count - 1):
        print(1 + adder, end=" ")
        pattern += 2
        adder += pattern
    print(1 + adder)


sequence_02(int(input()))
