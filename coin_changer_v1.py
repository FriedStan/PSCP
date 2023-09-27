"""CoinChangev1"""


def change_calc(change):
    """Give change the least coins as much as possible"""
    coin_list = [25, 10, 5]
    coin_used = 0
    for coin in coin_list:
        coin_used += change // coin
        change = change % coin
    print(coin_used + change)


change_calc(int(input()))
