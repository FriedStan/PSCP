"""https://open.spotify.com/track/7vJfDxu8HB8vLCiDDK8qLr?si=c7a4f5b8fa31446c"""


def main():
    """Main"""
    x_unit = int(input())
    y_unit = int(input())
    z_unit = int(input())
    out_1 = x_unit + 1
    out_2 = (7*(y_unit**3)) + (2*(y_unit**2)) - (31 * y_unit) + 1
    out_3 = z_unit * -1
    out_4 = (x_unit ** 2) - (y_unit ** 2)
    out_5 = (y_unit - (y_unit ** 2 - (4 * x_unit * z_unit)) ** 0.5) / (2 * x_unit)
    output = "{}\n{}\n{}\n{}\n{}".format(out_1, out_2, out_3, out_4, out_5)
    print(output)


main()
