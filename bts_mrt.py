"""BTSMRT"""


def children_day(age, height):
    """Age checker for children day"""
    if age < 14 and height <= 140:
        text = "FREE"
    else:
        text = "PAY"
    return text


def senior_day(age):
    """Age checker for Old people"""
    if age >= 60:
        text = "FREE"
    else:
        text = "PAY"
    return text


def free_or_not(special_day, age, height):
    """Make it free or pay"""
    if age < 14 and height < 90:
        text = "FREE"
    elif special_day.title() == "Children Day":
        text = children_day(age, height)
    elif special_day.title() == "Senior Day":
        text = senior_day(age)
    else:
        text = "PAY"
    print(text)


free_or_not(str(input()), float(input()), float(input()))
