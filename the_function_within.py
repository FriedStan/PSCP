"""https://open.spotify.com/track/3PJqRQ0nzw61pYA5zsWkaz?si=4e1fa6a2b7ef4489"""


def f_func(x_unit):
    """f function"""
    return 2 * x_unit


def g_func(x_unit):
    """g function"""
    result = (3 * x_unit ** 4) - (x_unit ** 3) + (2 * x_unit ** 2) + 10
    return result


def h_func(x_unit, y_unit, z_unit):
    """h function"""
    result = ((z_unit + x_unit) ** 2) - (x_unit * y_unit) + (y_unit ** 2)
    return result


def i_func(a_unit, b_unit, c_unit, d_unit):
    """i function"""
    result = ((a_unit ** 2) + (b_unit ** 2) - (c_unit ** 2)) / \
        ((d_unit ** 2) - (2 * a_unit * d_unit) + (2 * a_unit))
    return result


def main():
    """Main Func"""
    inp_a = float(input())
    inp_b = float(input())
    inp_c = float(input())
    inp_d = float(input())
    out_1 = f_func(f_func(inp_a))
    out_2 = g_func(f_func(inp_a - inp_b))
    out_3 = h_func(f_func(inp_a + inp_b), f_func(inp_a + inp_c), g_func(f_func(inp_d ** 2)))
    part_1 = h_func(f_func(inp_a + inp_b), f_func(inp_a - inp_c), g_func(f_func(inp_d ** 2)))
    part_3 = f_func(f_func(f_func(f_func(f_func(inp_c)))))
    out_4 = i_func(part_1, out_2, part_3, inp_d ** 8)
    output = "{}\n{}\n{}\n{}".format(out_1, out_2, out_3, out_4)
    print(output)


main()
