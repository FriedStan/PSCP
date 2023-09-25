"""Is Prime?"""


def will_it_prime(num):
    """Prime or not"""
    if num % 2 == 1:
        for i in iter(range(3, int(num ** 0.5) + 1, 2)):
            if (num / i).is_integer():
                return False
    return not(num in (0, 1) or (num % 2 == 0 and num != 2))


print(will_it_prime(int(input())))
