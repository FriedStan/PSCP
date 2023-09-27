"""Perfect"""


def unity(num):
    """Is that number perfect?"""
    factor = set()
    for i in iter(range(1, (num // 4) + 2)):
        if num % i == 0 and num != i:
            factor.add(i)
            if i != 1:
                factor.add(int(num / i))
    return sum(factor) == num


def precision(num):
    """use binary to find perfect number"""
    next_binary = "110"
    bin_to_dec = int(next_binary, 2)
    my_sum = 0
    while num >= bin_to_dec:
        if unity(bin_to_dec):
            my_sum += bin_to_dec
        next_binary = "1" + next_binary + "0"
        bin_to_dec = int(next_binary, 2)
    return my_sum


def perfection(num):
    """Sum of perfect number from 1 to num"""
    print(precision(num))



perfection(int(input()))
