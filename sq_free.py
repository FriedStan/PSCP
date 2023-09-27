"""SqFree"""


def sq_checker(num):
    """Check valid sq free number"""
    if num % 4 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % (i ** 2) == 0:
            return False
    return True


print(len(list(filter(sq_checker, iter(range(1, int(input()) + 1))))))
