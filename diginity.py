"""Diginity"""


def decoder(code):
    """Decode the code"""
    while code >= 10:
        summation = 0
        for num in str(code):
            summation += int(num)
        code = summation
    return code


def get_code():
    """Get code from input peoples"""
    code = int(input())
    while code != 0:
        print(decoder(code))
        code = int(input())


get_code()
