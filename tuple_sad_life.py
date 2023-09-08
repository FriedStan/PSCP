"""Tuple's Sad life"""


def sad_tuple(text, search):
    """Do as <e>judge says"""
    this_list = text.split()
    this_tuple = tuple(this_list)
    pos = this_tuple.index(search)
    size = this_tuple.count(search)
    for _ in range(size):
        print(((str(pos) + " ") * size).strip())


sad_tuple(str(input()), str(input()))
