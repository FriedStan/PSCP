"""PrasomSib"""


def stairway_to_ten(num_list):
    """https://youtu.be/ktgxMtWMflU?si=ixwR5deFKWU2_LMj"""
    count = 0
    for i, num in enumerate(num_list, 1):
        for things in num_list[i:]:
            num += things
            if num == 10:
                count += 1
                break
            if num > 10:
                break
    print(count)


stairway_to_ten(list(map(int, list(str(input()).strip()))))
