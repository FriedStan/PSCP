"""Is Prime?"""


def will_it_prime(num):
    """Prime or not"""
    text = "YES"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            text = "NO"
            break
    if num in (0, 1):
        text = "NO"
    print(text)


will_it_prime(int(input()))
