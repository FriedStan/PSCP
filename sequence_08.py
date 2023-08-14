"""Sequence VIII"""


def sequence_08(count):
    """Do as <e>judge said"""
    for i in range(1, count + 1):
        for _ in range(count - i):
            print("  ", end=" ")
        for k in range(1, i + 1):
            print("{:02d}".format(k), end=" ")
        print()


sequence_08(int(input()))
