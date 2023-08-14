"""Sequence IX"""


def sequence_09(count):
    """Do as <e>judge said"""
    for i in range(1, count + 1):
        for _ in range(count - i):
            print("  ", end=" ")
        for j in range(1, i + 1):
            print("{:02d}".format(j), end=" ")
        for k in range(i - 1, 0, -1):
            print("{:02d}".format(k), end=" ")
        print()


sequence_09(int(input()))
