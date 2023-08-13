"""Inflatation"""


def inflater(org_price, year):
    """Begin inflate"""
    inflate_rate = 3.81 / 100 # 3.81%
    inflate = 0
    for _ in range(year):
        inflate += (org_price + inflate) * inflate_rate
        inflate = (int(inflate * 100)) / 100
    print(org_price + inflate)


inflater(float(input()), int(input()))
