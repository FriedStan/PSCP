"""Seeker"""


def void_seeker(text):
    """Seek the answer"""
    num_list = []
    number = ""
    prev_char = ""
    for char in text:
        if char.isdigit():
            number += char
        elif char.isprintable() and prev_char.isdigit():
            num_list.append(int(number))
            number = ""
        prev_char = char
    if number.isdigit():
        num_list.append(int(number))
    print(sum(num_list))


void_seeker(str(input()))
