"""Heads and Legs"""


def kfc(all_unit, legs):
    """The Possibilities Are Endless"""
    if legs % 2 == 0:
        bird = min(legs // 2, all_unit)
        legs_have = bird * 2
        while legs_have < legs < all_unit * 4:
            bird -= 1
            legs_have += 2
        if (bird * 2) + ((all_unit - bird) * 4) == legs:
            print(all_unit - bird, bird)
        else:
            print("Impossible")
    else:
        print("Impossible")


kfc(int(input()), int(input()))
