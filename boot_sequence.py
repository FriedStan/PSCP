"""BootSequence"""


def sequencer(end_inp):
    """Print number from 1 to end_inp with _ as seperator"""
    for num in range(1, end_inp):
        print(num, end="_")
    print(end_inp)


sequencer(int(input()))
