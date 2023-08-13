"""Stepper I"""


def num_counter(end_inp):
    """Count the number from 1 to end_inp"""
    for _ in range(1, end_inp + 1):
        print(_)


num_counter(int(input()))
