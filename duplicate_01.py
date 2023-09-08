"""Duplicate I"""


def dupe(m_size, n_size):
    """Find the duplicate or nope"""
    set_m = set()
    set_n = set()
    for _ in range(m_size):
        set_m.add(str(input()))
    for _ in range(n_size):
        set_n.add(str(input()))
    set_dupe = set_m.intersection(set_n)
    if set_dupe == set():
        print("Nope")
    else:
        set_dupe = sorted(set_m.intersection(set_n), reverse=True)
        for things in set_dupe:
            print(things)


dupe(int(input()), int(input()))
