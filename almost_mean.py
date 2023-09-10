"""AlmostMean"""


def almost_mean(amount):
    """Find the one that almost pass mean"""
    id_dict = {}
    score_list = []
    summation = 0
    for _ in range(amount):
        text = str(input()).split()
        summation += float(text[1])
        score_list.append(float(text[1]))
        id_dict.update({float(text[1]): text[0]})
    mean = summation / amount
    score_list.append(mean)
    score_list.sort()
    pos = score_list.index(mean) - 1
    print("{}\t{}".format(id_dict[score_list[pos]], score_list[pos]))


almost_mean(int(input()))
