"""[Midterm 2022] Parity"""


def parity(bit, selected):
    """Make parity bit"""
    one = 0
    for things in bit:
        if things == "1":
            one += 1
    if selected.lower() == "even":
        if one % 2 == 0:
            print(bit + "0")
        else:
            print(bit + "1")
    else:
        if one % 2 == 0:
            print(bit + "1")
        else:
            print(bit + "0")


parity(str(input()), str(input()))
