"""Heads and Legs"""


def kfc(all_unit, legs):
    """The Possibilities Are Endless"""
    bird = min(legs // 2, all_unit)
    bird_leg = bird * 2
    need_leg = legs - bird_leg
    need_bunny = need_leg // 2
    new_bird = abs(bird - need_bunny)
    valid = (need_bunny * 4) + (new_bird * 2) == legs and need_bunny + new_bird == all_unit
    #print(bird, bird_leg)
    #print(need_leg, need_bunny)
    print("{} {}".format(need_bunny, new_bird) if valid else "Impossible")


kfc(int(input()), int(input()))
