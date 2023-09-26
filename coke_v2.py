"""[Midterm 2022] Coke"""


def cocacola_light():
    """Cocacola Normal cocacola ze ze zerooo"""
    normal_price = int(input())
    for_this_cap = int(input())
    discounted = int(input())
    wanted = int(input())
    if 0 not in (normal_price, wanted):
        try:
            free_cap = wanted // for_this_cap
            if wanted % for_this_cap == 0:
                free_cap -= 1
        except ZeroDivisionError:
            free_cap = 0
        wanted -= free_cap
        free_price = free_cap * discounted
        normal_pay = normal_price * wanted
        pay = free_price + normal_pay
        print(pay)
    else:
        print(0)


cocacola_light()
