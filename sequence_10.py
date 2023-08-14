"""Sequence X"""


def sequence_09_modified(count):
    """Do as <e>judge said"""
    for i in range(1, count):
        for _ in range(count - i):
            print("  ", end=" ")
        for j in range(1, i + 1):
            print("{:02d}".format(j), end=" ")
        for k in range(i - 1, 0, -1):
            print("{:02d}".format(k), end=" ")
        print()


def sequence_10(count):
    """Call sq 09(Modified) and do the other half"""
    sequence_09_modified(count)
    for i in range(count, 0, -1):
        for _ in range(count - i):
            print("  ", end=" ")
        for j in range(1, i):
            print("{:02d}".format(j), end=" ")
        for k in range(i, 0, -1):
            print("{:02d}".format(k), end=" ")
        print()


sequence_10(int(input()))
