"""PongYa"""


def pangya(num):
    """More like pongya"""
    print("PONG" if num % 3 == 0 or num % 10 == 3 else num)


pangya(int(input()))
