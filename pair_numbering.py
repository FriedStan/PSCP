"""PairNumbering"""
import json


def lets_pair(list_a, list_b, target):
    """pair number in list that sum = target"""
    needed = {}
    paired = 0
    for i in list_a:
        if i not in needed:
            needed.update({i: 1})
        else:
            needed[i] += 1
    for j in list_b:
        try:
            paired += needed.get(target - j)
        except TypeError:
            pass
    print(paired)


lets_pair(json.loads(str(input())), json.loads(str(input())), int(input()))
