"""Sequence XI"""


def sequence_11(count):
    """Do as <e>judge said"""
    size = (count * 2) - 1
    length = (count - 1) * -1
    adder = 1
    row_list = [1 for _ in range(size)]
    for row in range(length, count):
        index = 0
        for col in range(length, count):
            if abs(col) <= abs(row):
                row_list[index] = adder
            index += 1
        if row < 0:
            adder += 1
        else:
            adder -= 1
        for thing in row_list:
            print("{:02d}".format(thing), end=" ")
        print()


sequence_11(int(input()))
