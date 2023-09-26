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


def storm_caller(num, order_n):
    """For call fibo function"""
    if num <= order_n:
        if num + 900 <= order_n:
            fibonac_calc(num)
            storm_caller(num + 900, order_n)
        else:
            fibonac_calc(num)
            storm_caller(num + 1, order_n)


def main(order_n):
    """fibonacci at order_n"""
    if order_n not in (0, 1):
        storm_caller(2, order_n)
    print(FIBO_DICT.get(order_n))


main(int(input()))
