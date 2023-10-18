"""Compound Interest"""


def compound_calc(money, interest, year):
    """Calculate the compound interest"""
    try:
        final = money * (interest ** year)
    except OverflowError:
        interest /= 10
        final = money * (interest ** year)
    print("{:.2f}".format(final))


compound_calc(int(input()), 1 + (float(input()) / 100), int(input()))
