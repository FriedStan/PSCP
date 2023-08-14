"""Circular II"""


def mosquito_killer(x_me, y_me, x_friend, y_friend):
    """Calculate distance between point"""
    side_1 = x_friend - x_me
    side_2 = y_friend - y_me
    distance = (side_1 ** 2 + side_2 ** 2) ** 0.5
    return distance


def main():
    """Main func"""
    x_me = float(input())
    y_me = float(input())
    radius_me = float(input())
    x_friend = float(input())
    y_friend = float(input())
    radius_friend = float(input())
    distance = mosquito_killer(x_me, y_me, x_friend, y_friend)
    print("Yes" if radius_me + radius_friend > distance else "No")


main()
