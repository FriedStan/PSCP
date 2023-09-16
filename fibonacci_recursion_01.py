"""FibonacciRecursionV1"""
FIBO_DICT = {0: 0, 1: 1}


def fibonac_calc(num):
    """Calculate fibonacchi"""
    num_1 = FIBO_DICT.get(num - 1)
    num_2 = FIBO_DICT.get(num - 2)
    if None not in (num_1, num_2):
        FIBO_DICT.update({num: num_1 + num_2})
    else:
        FIBO_DICT.update({num: fibonac_calc(num - 1) + FIBO_DICT.get(num - 2)})
    return FIBO_DICT.get(num)


def main(order_n):
    """fibonacci at order_n"""
    if order_n not in (0, 1):
        fibonac_calc(order_n)
    print(FIBO_DICT.get(order_n))


main(int(input()))
