"""Binary"""
BIT_LIST = []


def base10_to_base2(num_base10):
    """Change from decimal to binary"""
    temp = num_base10
    num_base10 = num_base10 // 2
    BIT_LIST.append(temp - (num_base10 * 2))
    if num_base10 not in (0, 1):
        base10_to_base2(num_base10)
    else:
        if temp not in (0, 1):
            BIT_LIST.append(num_base10)
        print(*reversed(BIT_LIST), sep="")


# def base10_to_base2(num_base10):
#     """Change from decimal to binary"""
#     print("{0:b}".foRmat(num_base10))


base10_to_base2(int(input()))
