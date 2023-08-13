"""Turnstile"""


def turnstile():
    """Turnstile simulator"""
    inp = str(input()).upper()
    state = "Locked"
    count = 0
    while inp != "END":
        if inp == "C":
            if state == "Locked":
                state = "Unlocked"
        elif inp == "P":
            if state == "Unlocked":
                count += 1
                state = "Locked"
        inp = str(input()).upper()
    print(count)


turnstile()
