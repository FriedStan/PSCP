"""[Midterm 2022] Heron of Alexandria"""
from math import sqrt


def heron(num_a, num_b, num_c):
    """Calculate triangle area using Heron method"""
    num_s = (num_a + num_b + num_c) / 2
    area = sqrt(num_s * (num_s - num_a) * (num_s - num_b) * (num_s - num_c))
    return "{:.3f}".format(area)


print(heron(float(input()), float(input()), float(input())))
