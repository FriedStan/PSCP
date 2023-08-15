"""Milk"""


def milk_store(price, treshold, free, pocket):
    """Calculate free milk"""
    count = 0
    get_milk = 0
    while pocket >= price:
        get_milk += 1
        pocket -= price
        count += 1
        if count == treshold:
            get_milk += free
            count = free
    return get_milk


print(milk_store(int(input()), int(input()), int(input()), int(input())))
