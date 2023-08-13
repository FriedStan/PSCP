"""Lotto more like Lotte"""


def get_prize():
    """Get prize number"""
    prize_1 = str(input())
    prize_2back = str(input())
    prize_3front_1 = str(input())
    prize_3front_2 = str(input())
    prize_3back_1 = str(input())
    prize_3back_2 = str(input())
    return prize_1, prize_2back, prize_3front_1, prize_3front_2, prize_3back_1, prize_3back_2


def lotto_checker():
    """Check your lotto"""
    prize_1, prize_2back, prize_3front_1, prize_3front_2, prize_3back_1, prize_3back_2 \
        = get_prize()
    your_lotto = str(input())
    money = 0
    low = str(int("10" + prize_1) - 1)[2:]
    high = str(int("10" + prize_1) + 1)[2:]
    if prize_1 == "000000":
        low += "9"
    if your_lotto == prize_1:
        money += 6_000_000
    if your_lotto[4:7] == prize_2back:
        money += 2_000
    if your_lotto[0:3] in (prize_3front_1, prize_3front_2):
        money += 4_000
    if your_lotto[3:7] in (prize_3back_1, prize_3back_2):
        money += 4_000
    if your_lotto in (low, high):
        money += 100_000
    print(low, high)
    print(money)


lotto_checker()
