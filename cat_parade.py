"""Cat Parade"""


def cat_parade(cat_type):
    """Just a Cat patade"""
    cat_list = []
    while cat_type != "END":
        if cat_type != "IT'S A DOG":
            current_cat = cat_type.split(", ")
            cat_list.extend(current_cat)
        else:
            cat_list.pop(len(cat_list) - 1)
        cat_type = str(input())
    cat_list_sort = cat_list.copy()
    cat_list_sort.sort()
    cat_set_sort = sorted(list(set(cat_list_sort)))
    for things in cat_set_sort:
        print("{} {} {}".format(things, (cat_list.index(things) + 1), cat_list.count(things)))


cat_parade(str(input()))
