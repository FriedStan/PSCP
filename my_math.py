"""MyMath"""
from math import sin, cos, log, radians, factorial, sqrt


def main():
    """Main Func"""
    out_1 = (sin(radians(90)) + (pow(sin(radians(60)), 2))) / \
        (cos(radians(pow(245, 2))) + cos(radians(45 + 135)))
    out_2 = factorial(16) * factorial(4) / factorial(8)
    out_3 = (15 + 25) / sqrt(pow((25 - 12), 2) + pow((12 - 15), 2))
    out_4 = log(pow(1234, 4), 10)
    out_5 = (log(4234, 5) + log(8191, 2) + 71 * log(156154, 10)) / \
        (log(777, 7) - log(888, 8) - log(999, 9))
    output = "{}\n{}\n{}\n{}\n{}".format(out_1, out_2, out_3, out_4, out_5)
    print(output)


main()
