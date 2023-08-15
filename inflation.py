"""Inflatation"""


def inflater(org_price, year):
    """Begin inflate"""
    inflate_rate = 381  # 3.81%
    price = int(org_price * 100)
    for _ in range(year):
        price = (price * 10000 + (price * inflate_rate)) // 10000
    print("{}.{:02d}".format(price // 100, price % 100))


inflater(float(input()), int(input()))
