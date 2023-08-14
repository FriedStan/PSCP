"""Restaurant"""


def restaurant_trick(org_price, promotion, discount, offer):
    """Trick of the trade"""
    pay_price = org_price + offer
    if pay_price >= promotion:
        get_discount = pay_price * (discount / 100)
    else:
        get_discount = 0
    if get_discount > offer:
        result = "Yes {:.3f}".format(get_discount - offer)
    elif get_discount < offer:
        result = "No {:.3f}".format(offer - get_discount)
    else:
        result = "Yes"
    return result


print(restaurant_trick(float(input()), float(input()), float(input()), float(input())))
