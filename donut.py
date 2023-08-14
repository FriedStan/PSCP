"""Donut"""


def donut_store(u_a, u_b, u_c, u_d):
    """Sell donut to customer"""
    free_count = 0
    money = 0
    current_donut = 0
    while current_donut < u_d:
        current_donut += 1
        money += u_a
        free_count += 1
        if free_count == u_b:
            current_donut += u_c
            free_count = 0
    return "{} {}".format(money, current_donut)


def main():
    """Main func"""
    print(donut_store(int(input()), int(input()), int(input()), int(input())))


main()
