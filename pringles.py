"""Pringles"""


def pringle():
    """Pringle"""
    side_a = str(input())
    inside = str(input())
    side_b = str(input())
    finger = int(input())
    get_chips = 0
    for _ in range(inside.count(")")):
        chips_pos = inside.find(")")
        if chips_pos + 1 <= finger:
            inside = inside.replace(")", " ", 1)
            get_chips += 1
    print(get_chips)
    if inside.count(")") >= 1:
        print("There are still some left.")
    else:
        print("None.")
    print(side_a)
    print(inside)
    print(side_b)


pringle()
