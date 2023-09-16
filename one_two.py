"""OneTwo"""
MEM_DICT = {1: "1", 2: "2"}


def looper(order_n):
    """Loop and add dict"""
    text_01 = MEM_DICT.get(order_n - 1)
    text_02 = MEM_DICT.get(order_n - 2)
    if None not in (text_01, text_02):
        MEM_DICT.update({order_n: text_01 + text_02})
    else:
        MEM_DICT.update({order_n: looper(order_n - 1) + MEM_DICT.get(order_n - 2)})
    return MEM_DICT.get(order_n)


def the_connector(order_n):
    """do as <e>judge says"""
    if order_n not in (1, 2):
        looper(order_n)
    print(MEM_DICT.get(order_n))


the_connector(int(input()))
