"""Stepper II"""


def num_counter(start_inp, end_inp):
    """Count the number from start_inp to end_inp"""
    if end_inp >= start_inp:
        for num in range(start_inp, end_inp + 1, 1):
            print(num)
    else:
        for num in range(start_inp, end_inp - 1, -1):
            print(num)


num_counter(int(input()), int(input()))
