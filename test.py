"""Bridge"""


def bridge_crosser(b_1, b_2, b_3):
    """Count the times the you cross the bridge"""
    l_list = [b_1, b_2, b_3]
    r_list = []
    time = 0
    while l_list:
        picked = l_list[0]
        if picked != "chicken" and not r_list:
            l_list.append(picked)
            l_list.pop(0)
            continue
        r_list.append(picked)
        l_list.pop(0)
        time += 1
        if "chicken" in r_list and "dog" in r_list:
            picked = r_list[0]
            l_list.append(r_list)
            r_list.pop(0)
            time += 1
        elif "chicken" in r_list and "veggies" in r_list:
            picked = r_list[0]
            l_list.append(r_list)
            r_list.pop(0)
            time += 1
    print(time)



bridge_crosser(str(input()), str(input()), str(input()))