"""OTP"""


def eight(histo_g):
    """For 6 char"""
    three_2 = 0
    two_3 = 0
    for value in histo_g.values():
        if value == 2:
            two_3 += 1
        elif value == 3:
            three_2 += 1
    if three_2 != 2 and two_3 != 3:
        return "Invalid"
    return "Valid"


def six(histo_g):
    """For 6 char"""
    two_2 = 0
    one_3 = 0
    for value in histo_g.values():
        if value == 2:
            two_2 += 1
        elif value == 3:
            one_3 += 1
    if two_2 != 2 and one_3 != 1:
        return "Invalid"
    return "Valid"


def four(histo_g):
    """For 4 char"""
    dupe = 0
    for _, amount in histo_g.items():
        if amount == 2:
            dupe += 1
        elif amount > 2:
            return "Invalid"
    if dupe != 1:
        return "Invalid"
    return "Valid"


def otp_validator(current_otp):
    """TPO TOP POT PTO"""
    things = []
    while current_otp != "0":
        size = len(current_otp)
        current_histogram = {}
        for char in current_otp:
            current_histogram[char] = current_histogram.get(char, 0) + 1
        if size == 4:
            things.append(four(current_histogram))
        elif size == 6:
            things.append(six(current_histogram))
        elif size == 8:
            things.append(eight(current_histogram))
        current_otp = str(input())
    print(*things, sep="\n")


otp_validator(str(input()))
