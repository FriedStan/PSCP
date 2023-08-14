"""Sequence III"""


def sequence_03(count):
    """Do as <e>judge said"""
    for i in range(2, count + 2):
        for j in range(i, count + i):
            print(j, end=" ")
        print()



sequence_03(int(input()))
