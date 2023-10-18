"""Tax"""


def taxing(year, power):
    """Tax the car"""
    tax_percent = {6: 0.9, 7: 0.8, 8: 0.7, 9: 0.6, 10: 0.5}
    get_tax = tax_percent.get(year)
    if year > 10:
        get_tax = 0.5
    elif year < 6:
        get_tax = 1
    first_take = 300 if power >= 600 else power * 0.5
    power -= 600
    second_take = 1800 if power >= 1200 else max(power, 0) * 1.5
    power -= 1200
    third_take = max(power, 0) * 4
    print("{:.2f}".format((first_take + second_take + third_take) * get_tax))


taxing(int(input()), int(input()))
