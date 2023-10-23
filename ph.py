"""PH"""


def ph_chart(point):
    """Ph chart"""
    if 0 <= point < 7:
        print("acidic")
    elif point == 7:
        print("neutral")
    elif 7 < point <= 14:
        print("akaline")
    else:
        print("error")


ph_chart(float(input()))
