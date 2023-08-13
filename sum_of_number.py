"""SumOfNumber"""


def loop_summation(target_inp):
    """
    Loop until user input -1 or summation equal to target user input
    then print the summation of all previous number
    """
    num_sum = 0
    num_inp = int(input())
    while num_inp != -1 and num_sum != target_inp:
        num_sum += num_inp
        if num_sum != target_inp:
            num_inp = int(input())
    return num_sum


print(loop_summation(int(input())))
