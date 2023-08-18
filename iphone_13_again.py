"""Iphone 13"""


def iphone_verifyer(that_iphone):
    """Verify iPhone"""
    that_iphone = that_iphone.replace(" ", "")
    return that_iphone[6:]


def iphone_13_mini(capacity):
    """Verify capacity for iP13 mini"""
    if capacity == "128 GB":
        price = 25900
    elif capacity == "256 GB":
        price = 29900
    elif capacity == "512 GB":
        price = 37900
    else:
        price = "Not Available"
    return price


def iphone_13(capacity):
    """Verify capacity for iP13"""
    if capacity == "128 GB":
        price = 29900
    elif capacity == "256 GB":
        price = 33900
    elif capacity == "512 GB":
        price = 41900
    else:
        price = "Not Available"
    return price


def iphone_13_pro(capacity):
    """Verify capacity for iP13 pro"""
    if capacity == "128 GB":
        price = 38900
    elif capacity == "256 GB":
        price = 42900
    elif capacity == "512 GB":
        price = 50900
    elif capacity in ("1 TB", "1024 GB"):
        price = 58900
    else:
        price = "Not Available"
    return price


def iphone_13_promax(capacity):
    """Verify capacity for iP13 promax"""
    if capacity == "128 GB":
        price = 42900
    elif capacity == "256 GB":
        price = 46900
    elif capacity == "512 GB":
        price = 54900
    elif capacity in ("1 TB", "1024 GB"):
        price = 62900
    else:
        price = "Not Available"
    return price


def iphone_checker(that_iphone, capacity):
    """Tell the price"""
    if that_iphone[:6] == "iPhone":
        that_iphone = iphone_verifyer(that_iphone).lower()
        if that_iphone == "13mini":
            price = iphone_13_mini(capacity)
        elif that_iphone == "13":
            price = iphone_13(capacity)
        elif that_iphone == "13pro":
            price = iphone_13_pro(capacity)
        elif that_iphone == "13promax":
            price = iphone_13_promax(capacity)
        else:
            price = "Not Available"
    else:
        price = "Not Available"
    print(price)


iphone_checker(str(input()), str(input()).upper())
