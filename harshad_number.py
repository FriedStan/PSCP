"""Harshad Number"""


def harshad_checker(num):
    """Check that number is Harshad of not"""
    harshad = 0
    for i in str(num):
        harshad += int(i)
    if harshad != 0:
        if num % harshad == 0:
            text = "Yes"
        else:
            text = "No"
    else:
        text = "No"
    return text


def get_num():
    """Get input the check it"""
    for _ in range(10):
        print(harshad_checker(abs(int(input()))))


get_num()
