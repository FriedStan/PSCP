"""[Midterm 2022] Coke"""


def cocacola_light():
    """Cocacola Normal cocacola ze ze zerooo"""
    normal_price = int(input())
    for_this_cap = int(input())
    discounted = int(input())
    wanted = int(input())
    current_cap = 0
    pay = 0
    while wanted > 0:
        if current_cap < for_this_cap or for_this_cap == 0:
            current_cap += 1
            pay += normal_price
        elif current_cap >= for_this_cap:
            current_cap -= for_this_cap
            current_cap += 1
            pay += discounted
        wanted -= 1
    print(pay)


cocacola_light()
