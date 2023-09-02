"""Gotta catch them all"""


def saint_loop(sec, punch):
    """Loop"""
    attack = 0
    current_sec = 0
    while attack < punch and current_sec <= sec / 2:
        current_sec += 1
        if sec % 2 == 0:
            if current_sec % 3 == 0:
                attack += 1
            else:
                attack += 165
        else:
            if current_sec % 3 == 0:
                attack += 1
            elif current_sec == int(sec / 2):
                pass
            else:
                attack += 165
    rolling_crash = sec - (current_sec * 2)
    if rolling_crash > 0:
        sec -= 1
    rolling_crash = sec - (current_sec * 2)
    rolling_crash = max(rolling_crash, 0)
    print(attack + rolling_crash * 12)


saint_loop(int(input()), int(input()))
