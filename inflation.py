"""Inflatation"""


def inflater(org_price, year):
    """Begin inflate"""
    inflate_rate = 0.0381  # 3.81%
    price = int(org_price * 100)
    for _ in range(year):
        price = price + price * inflate_rate
        decimal = str(price).find(".")
        price = int(str(price)[:decimal])
    print("{:.2f}".format(price))


inflater(float(input()), int(input()))
