"""Difference"""


def diff(a_size, b_size):
    """Set A - Set B"""
    set_a = set()
    set_b = set()
    for _ in range(a_size):
        set_a.add(int(input()))
    for _ in range(b_size):
        set_b.add(int(input()))
    set_c = sorted(set_a.difference(set_b))
    for num in set_c:
        print(num, end=" ")


diff(int(input()), int(input()))
