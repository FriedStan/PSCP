"""Filter"""
import json


def filter_the_score(dict_text, score_filter):
    """Filter the score that user input"""
    score_dict = json.loads(dict_text)
    score_list = list(score_dict.items())
    score_list.sort(key=lambda val: int(val[0]))
    just_print = False
    for things in score_list:
        if float(things[1]) < score_filter:
            continue
        print("{}\t{:.2f}".format(things[0], things[1]))
        just_print = True
    if just_print is False:
        print("Nope")


filter_the_score(str(input()), float(input()))
