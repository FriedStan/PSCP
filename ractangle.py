"""https://open.spotify.com/track/6ugrRFZUNIpLiqhLUgC7ix?si=372c738075774aab"""


def rectangle_area(h_unit, w_unit):
    """Calculate area of the rectangle"""
    print(h_unit * w_unit)


def rectangle_perimeter(h_unit, w_unit):
    """Calculate perimeter of the rectangle"""
    print((h_unit * 2) + (w_unit * 2))


def main():
    """Main Func"""
    height = int(input())
    width = int(input())
    rectangle_area(height, width)
    rectangle_perimeter(height, width)


main()
