"""HowLong"""


def digit_total(num_inp):
    """Count the digit of the number user input"""
    digit = 0
    for num in str(num_inp):
        if num.isdigit():
            digit += 1
    return digit


print(digit_total(int(input())))
