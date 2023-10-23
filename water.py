"""Water"""


def watering():
    """Water"""
    month = int(input())
    per_cm3 = float(input())
    treshold = float(input())
    after_per_cm3 = float(input())
    free_baht = float(input())
    usage_per_month = [float(input()) for _ in range(month)]
    payment = 0
    for things in usage_per_month:
        this_mon_pay = 0
        this_mon_pay += min(things, treshold) * per_cm3
        things -= treshold
        this_mon_pay += max(things, 0) * after_per_cm3
        payment += 0 if this_mon_pay <= free_baht else this_mon_pay
    return "{:.2f}".format(payment)


print(watering())
