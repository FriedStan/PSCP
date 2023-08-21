"""[Midterm 2022] Calculator"""


def calc_button(num):
    """Count each button pressed"""
    seq = ""
    for i in range(1, num):
        seq += str(i) + "+"
    seq += str(num) + "="
    print(len(seq) if num != 1 else 1)


calc_button(int(input()))
