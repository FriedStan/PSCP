"""MissingNumber"""


def missing_number(num_range):
    """Use set to help"""
    num_set = set()
    full_set = set(range(1, num_range + 1))
    num = int(input())
    while num != 0:
        num_set.add(num)
        num = int(input())
    missing = sorted(full_set.difference(num_set))
    for things in missing:
        print(things)


missing_number(int(input()))
