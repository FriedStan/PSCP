"""PairNumbering"""
import json


def lets_pair(list_a, list_b, target):
    """pair number in list that sum = target"""
    maxine = dict((i, '') for i in list_a)
    minna = dict((i, '') for i in list_b)
    total = dict((i, target - i) for i in minna)
    print(total)
    print(maxine)
    print(minna)
    #print(len(list(filter(lambda i: i[0] + i[1] == target,\
    # iter((a, b) for a in list_a for b in list_b)))))
    #print(len([(a, b) for a in list_a for b in list_b if a + b == target]))


lets_pair(json.loads(str(input())), json.loads(str(input())), int(input()))
