"""https://open.spotify.com/track/7G1mpcB5NMRMUidZZdd9Mj?si=6237405b39b64753"""
from math import sqrt


def main():
    """Main func"""
    q_1 = float(input())
    q_2 = float(input())
    p_1 = float(input())
    p_2 = float(input())
    print(sqrt(pow(q_1 - p_1, 2) + pow(q_2 - p_2, 2)))


main()
