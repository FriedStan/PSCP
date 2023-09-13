"""CuteCat CuteFox"""


def type_number_sorting(that_list):
    """For sort Fox/Cat by number"""
    return int(that_list[1][3:])


def cat_or_fox(pack_size):
    """https://youtu.be/XuJGCuXOkjg?si=4KkmQ3IIUjmmOti-"""
    cat_list = []
    fox_list = []
    for _ in range(pack_size):
        that_json = str(input())
        pos = that_json.find(":")
        text = that_json[2: pos - 2], that_json[pos + 3:len(that_json) - 2]
        this_animal = text
        if "Cat" in this_animal[1].title():
            cat_list.append(this_animal)
        elif "Fox" in this_animal[1].title():
            fox_list.append(this_animal)
    cat_name_order = (tuple(zip(("_", "_"), *cat_list)))
    fox_name_order = (tuple(zip(("_", "_"), *fox_list)))
    if "Garfield" not in cat_name_order[0] + fox_name_order[0] and\
            "Cat01" not in cat_name_order[1]:
        cat_list.append(("Garfield", "Cat01"))
    if "Fubuki" not in cat_name_order[0] + fox_name_order[0] and\
            "Fox01" not in fox_name_order[1]:
        fox_list.append(("Fubuki", "Fox01"))
    cat_list.sort(key=type_number_sorting)
    fox_list.sort(key=type_number_sorting)
    print("Cat : {}\nFox : {}".format(len(cat_list), len(fox_list)))
    for cat in cat_list:
        print("{} : {}".format(cat[0], cat[1]))
    for fox in fox_list:
        print("{} : {}".format(fox[0], fox[1]))


cat_or_fox(int(input()))
