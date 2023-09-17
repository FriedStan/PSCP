"""RectangleArea"""


def overlapper(rec1_text, rec2_text):
    """Is the rectangle overlap?"""
    rec1 = list(map(int, rec1_text.split()))
    rec2 = list(map(int, rec2_text.split()))
    set_w1 = set(i + rec1[0] for i in range(rec1[2]))
    set_w2 = set(i + rec2[0] for i in range(rec2[2]))
    set_h1 = set(i + rec1[1] for i in range(rec1[3]))
    set_h2 = set(i + rec2[1] for i in range(rec2[3]))
    width = len(set_w1.intersection(set_w2))
    height = len(set_h1.intersection(set_h2))
    intersec = width and height
    if intersec:
        print(width * height)
    else:
        print("no overlapping")


overlapper(str(input()), str(input()))
