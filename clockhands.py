"""ClockHands"""


def will_it_collapse(hour, minute):
    """Look that will the each clockhands will collapse each other"""
    collapse = False
    minute_hand = (minute // 5, (minute - ((minute // 5) * 5)) * 20)
    hour_hand = (hour, (minute / 60) * 100)
    diff = hour_hand[1] - minute_hand[1]
    if hour_hand[0] == minute_hand[0] and 0 <= diff < 20:
        collapse = True
    print(collapse)


will_it_collapse(int(input()), int(input()))
