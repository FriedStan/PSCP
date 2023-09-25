"""Is Prime?"""


def will_it_prime(num):
    """Prime or not"""
    for i in iter(range(2, int(num ** 0.5) + 1)):
        if num % i == 0:
            return "NO"
    return "YES" if num not in (0, 1) else "NO"


print(will_it_prime(int(input())))
