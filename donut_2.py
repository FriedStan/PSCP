"""Donut"""


def donut_store(price, free_threshold, free_donut, need_donut):
    """Sell donut to customer"""
    buy_times = need_donut // (free_threshold + free_donut)
    need_more = need_donut % (free_threshold + free_donut)
    money = buy_times * (price * free_threshold)
    donut = buy_times * (free_threshold + free_donut)
    if need_more >= free_threshold:
        free_count = need_more // free_threshold
        donut += free_count * (free_threshold + free_donut)
        money += free_count * (price * free_threshold)
    else:
        donut += need_more
        money += need_more * price
    return "{} {}".format(money, donut)


def main():
    """Main func"""
    print(donut_store(int(input()), int(input()), int(input()), int(input())))


main()
