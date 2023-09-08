"""PickThem"""
from json import loads


def pick_them(this_str):
    """Do as <e>judge says"""
    this_list = loads(this_str)
    even = False
    for things in this_list:
        if things % 2 == 0:
            print(things)
            even = True
    if even is False:
        print("Nope")


pick_them(str(input()))
