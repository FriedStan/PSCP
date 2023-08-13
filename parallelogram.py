"""Parallelogram"""


def en_pisa(text):
    """Make text เอียง"""
    size = len(text)
    for i in range(size, 0, -1):
        print(" " * (i - 1) + text[0:abs(size - i) + 1])
    for i in range(1, size):
        print(text[i:size])


en_pisa(str(input()))
