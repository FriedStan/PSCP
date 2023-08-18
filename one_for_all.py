"""Full cowling"""


def one_for_all(generation):
    """Transport quirk and will to the next generation"""
    link = ""
    for gen in range(1, generation + 1):
        name = str(input())
        if gen == generation:
            link += name + "_{}".format(gen)
        elif gen % 2 == 0:
            link += name + "-" * gen
        else:
            link += name + "*" * gen
    print(link)


one_for_all(int(input()))
