"""Poisonous Vegetables"""


def stardew(size):
    """Dewdrop"""
    each_area = int(input())
    day_need = int(input())
    garden = list(map(lambda x: list(map(lambda z: list(map(int, z.split())), filter(any, map(
        lambda y: y.replace("]", ""), x.split("["))))), [str(input()) for _ in range(size[0])]))
    for row in garden:
        for col in row:
            text = "x"
            if col[2] >= col[0] and col[0] <= day_need and col[0] - col[2] >= 0:
                text = "o"
            if col[1] > each_area:
                text = "-"
            print("[ {} ]".format(text), end="")
        print()


stardew(list(map(int, str(input()).split(" x "))))
