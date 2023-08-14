"""RuleofThree"""


def find_worthest(price, size):
    """Find the worthest snacks"""
    return size / price


def how_many_snacks(pack):
    """Get snack package"""
    price = float(input())
    size = float(input())
    old_price = find_worthest(price, size)
    worthest_price = price
    worthest_size = size
    for _ in range(pack - 1):
        price = float(input())
        size = float(input())
        price_per_b = find_worthest(price, size)
        if price_per_b != old_price:
            if price_per_b > old_price:
                worthest_price = price
                worthest_size = size
                old_price = price_per_b
        else:
            if worthest_price >= price:
                worthest_price = price
                worthest_size = size
    print("{:.2f} {:.2f}".format(worthest_price, worthest_size))


how_many_snacks(int(input()))
