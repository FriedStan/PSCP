"""Gram_v1"""


def gram_calc(text, g_size):
    """Find the char that stick together by g_size"""
    prep = []
    for i in range(g_size - 1, -1, -1):
        prep.append(text.copy()[:len(text) - i])
        text.pop(0)
    cooked = list(zip(*prep))
    serve = {i: cooked.count(i) for i in cooked}
    table = sorted(serve, key=serve.get, reverse=True)
    print("{}\n{}".format("".join(table[0]), serve.get(table[0])))


gram_calc(list(str(input())), 2)
