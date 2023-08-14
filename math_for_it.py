"""https://open.spotify.com/track/3xhbFPgrYiWY7Oz3qovZuj?si=1ddb99e0024242a8"""
from math import pi


def main():
    """Main Func"""
    radius = float(input())
    print("Area: %.3f" % (pi * (radius ** 2)))
    print("Circumference: %.3f" % (2 * pi * radius))


main()
