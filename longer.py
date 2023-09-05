"""[Midterm 2023] Longer"""
from math import pi


def compareraretor(radius, side_a, side_b):
    """Compare the Circle & the Rectangle"""
    circle_circ = 2 * pi * radius
    rectangle_circ = (side_a + side_b) * 2
    diff = abs(circle_circ - rectangle_circ)
    if circle_circ > rectangle_circ:
        text = "Circle is longer"
    elif rectangle_circ > circle_circ:
        text = "Rectangle is longer"
    else:
        text = "Equal"
    print(text + "\n%.5f" % diff)


compareraretor(float(input()), float(input()), float(input()))
