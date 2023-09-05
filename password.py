"""[Midterm 2023] Password"""
from math import log


def pool_checker(password):
    """Return pool size"""
    alpha_low = False
    alpha_upp = False
    number = False
    special = False
    pool_size = 0
    for things in password:
        if things.islower() and alpha_low is False:
            pool_size += 26
            alpha_low = True
        if things.isupper() and alpha_upp is False:
            pool_size += 26
            alpha_upp = True
        if things.isdigit() and number is False:
            pool_size += 10
            number = True
        if not things.isalnum() and special is False:
            pool_size += 32
            special = True
    return pool_size


def entropy_checker(entropy):
    """Return how strong is your password"""
    if entropy < 28:
        text = "Very Weak"
    elif 28 <= entropy <= 35:
        text = "Weak"
    elif 36 <= entropy <= 59:
        text = "Reasonable"
    elif 60 <= entropy <= 127:
        text = "Strong"
    else:
        text = "Very Strong"
    return text


def password_checker(password):
    """Check your password"""
    pool_size = pool_checker(password)
    entropy = int(log(pool_size ** len(password), 2))
    how_strong = entropy_checker(entropy)
    print("%d\n%s" % (entropy, how_strong))


password_checker(str(input()))
