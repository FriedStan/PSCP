"""Circular I"""


def mosquito_killer(x_me, y_me, x_mosquito, y_mosquito):
    """Calculate distance between point"""
    side_1 = x_mosquito - x_me
    side_2 = y_mosquito - y_me
    distance = (side_1 ** 2 + side_2 ** 2) ** 0.5
    return distance


def main():
    """Main func"""
    x_me = float(input())
    y_me = float(input())
    radius = float(input())
    x_mosquito = float(input())
    y_mosquito = float(input())
    distance = mosquito_killer(x_me, y_me, x_mosquito, y_mosquito)
    print("Yes" if radius >= distance else "No")


main()
