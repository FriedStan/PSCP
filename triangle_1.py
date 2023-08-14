"""Triangle 1"""


def tri_maker(tri_list):
    """Making triangle"""
    big = 0
    tri_sum = 0
    for tri in tri_list:
        if big <= tri:
            big = tri
        else:
            pass
    for tri in tri_list:
        if tri == big:
            pass
        else:
            tri_sum += tri ** 2
    if abs(tri_sum - big ** 2) <= 0.01:
        result = "Yes"
    else:
        result = "No"
    return result


def main():
    """Main func"""
    tri_3 = []
    for _ in range(3):
        tri_3.append(float(input()))
    print(tri_maker(tri_3))


main()
