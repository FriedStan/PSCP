"""[Midterm 2023] Niwarn World"""
from math import log, sin, radians, sqrt


def x_calc(n_pt):
    """Calculate X pos"""
    x_top = log(n_pt ** 2, 2)
    x_bot = (2 * n_pt) * log(n_pt, 2)
    x_pos = 2 + (x_top / x_bot)
    return x_pos


def y_calc(n_pt, s_pt):
    """Calculate Y pos"""
    y_top = sin(radians(30)) + sqrt(2 * s_pt)
    y_bot = x_calc(n_pt) + 3
    y_pos = y_top / y_bot
    return y_pos


def z_calc(k_pt):
    """Calculate Z pos"""
    z_top = 8456 * (x_calc(k_pt) ** 4)
    z_bot = 24 * k_pt
    z_pos = (y_calc(k_pt, k_pt) ** 2) + (z_top / z_bot)
    return z_pos


def niwarn_t4e(n_pt, s_pt, k_pt):
    """Niwarn position"""
    x_pos = x_calc(n_pt)
    y_pos = y_calc(n_pt, s_pt)
    z_pos = z_calc(k_pt)
    print("X: %.1f, Y: %.1f, Z: %.1f" % (x_pos, y_pos, z_pos))


niwarn_t4e(float(input()), float(input()), float(input()))
