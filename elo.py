"""Elo rating"""


def elo_calc(r_a, r_b, user_select):
    """Calculate Elo"""
    if user_select == "A":
        elo_out = 1 / (1 + (10 ** ((r_b - r_a) / 400)))
    else:
        elo_out = 1 / (1 + (10 ** ((r_a - r_b) / 400)))
    return "{:.2f}".format(elo_out)


print(elo_calc(int(input()), int(input()), str(input()).upper()))
