"""Stamp"""


def stamper(that_money, every_that_money, get_stamp, stamp):
    """Stamp the card"""
    stamp += (that_money // every_that_money) * get_stamp
    return stamp


def discounter(payment, that_stamp, every_that_stamp, discount_by):
    """Calculate discount"""
    discounted = 0
    if that_stamp > 0:
        while discounted < payment and that_stamp >= every_that_stamp:
            discounted += discount_by
            that_stamp -= every_that_stamp
    return discounted, that_stamp


def promotion_calculator():
    """Calculate promotion"""
    dine_in_times = int(input())
    every_that_money = int(input())
    get_stamp = int(input())
    every_that_stamp = int(input())
    discount_by = int(input())
    sum_payment = 0
    stamp = 0
    for _ in range(dine_in_times):
        payment = int(input())
        discounted, stamp = discounter(payment, stamp, every_that_stamp, discount_by)
        if payment - discounted >= 0:
            payment = payment - discounted
        else:
            payment = 0
        stamp = stamper(payment, every_that_money, get_stamp, stamp)
        sum_payment += payment
    print(sum_payment)
    print(stamp)


promotion_calculator()
