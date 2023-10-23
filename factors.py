"""Factors"""


def prime_checker(num):
    """Check that num is prime"""
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_the_factors(amount):
    """Factors"""
    num_factor = []
    factor = []
    for _ in range(amount):
        num = int(input())
        count = 2
        while prime_checker(num) is False:
            if num % count == 0:
                num = num / count
                factor.append(count)
            else:
                count += 1
        factor.append(int(num))
        num_factor.append(factor.copy())
        factor.clear()
    for i, things in enumerate(num_factor.copy()):
        num_factor[i] = {}
        count = 1
        text = ""
        for num in things:
            num_factor[i][num] = num_factor[i].get(num, 0) + 1
        for key, value in num_factor[i].items():
            if value > 1:
                text += "{}**{}".format(key, value)
            else:
                text += str(key)
            if count != len(num_factor[i]):
                text += " x "
            count += 1
        print(text)


find_the_factors(int(input()))
