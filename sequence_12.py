"""Sequence XII"""


def sequence_12(count):
    """Do as <e>judge said"""
    length = (count * -1) + 1
    for row in range(length, count):
        for col in range(length, count):
            num = count - abs(abs(row) - abs(col))
            print("{:02d}".format(num), end=" ")
        print()


sequence_12(int(input()))
