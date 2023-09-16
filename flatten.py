"""Flatten"""
import json
OUT_LIST = []


def dough_maker(text_list):
    """make a crossaint"""
    for things in text_list:
        if isinstance(things, list):
            dough_maker(things)
        else:
            OUT_LIST.append(things)


def bread_flattener(text):
    """sort the crossaint"""
    text_list = json.loads(text)
    dough_maker(text_list)
    print(sorted(OUT_LIST, reverse=True))


bread_flattener(str(input()))
