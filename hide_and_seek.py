"""HideAndSeek"""


def num_counter(start_inp, end_inp, step_inp):
    """Count the number from start_inp to end_inp-1 by step_inp"""
    for num in range(start_inp, end_inp, step_inp):
        print(num)


num_counter(int(input()), int(input()), int(input()))
