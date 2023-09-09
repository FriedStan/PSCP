"""Gotta catch them all"""
from math import ceil


def saint_loop(sec, punch):
    """Loop"""
    attack = 0
    one_set = 331 # 6 sec
    set_punch = punch // 331
    set_attack = sec // 6
    if punch >= one_set:
        if min(set_punch, set_attack) == set_punch:
            sec -= set_punch * 6
            attack += one_set * set_punch
        elif min(set_punch, set_attack) == set_attack:
            attack += one_set * set_attack
            sec -= set_attack * 6
    if attack < punch:
        attack_left = abs(punch - attack)
        ryu_punch = max(ceil(attack_left / 165), 1)
        if sec - (ryu_punch * 2) < 0:
            can_attack = sec // 2
            attack += can_attack * 165
            sec -= can_attack * 2
        else:
            attack += ryu_punch * 165
            sec -= ryu_punch * 2
    print(attack + (12 * max(sec - 1, 0)))


saint_loop(int(input()), int(input()))
