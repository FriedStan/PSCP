"""Compound Interest"""


def compound_calc(money, interest, year):
    """Calculate the compound interest"""
    final = money * (interest ** year)
    print("{}".format(str(final)))


compound_calc(int(input()), (100 + float(input())) / 100, int(input()))
