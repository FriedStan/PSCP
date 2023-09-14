"""[Midterm 2023] Distribute"""


def distribute(money, child):
    """[Midterm 2023] Distribute"""
    if money >= child:
        money -= child
        successfull_8 = min(money // 7, child)
        money -= successfull_8 * 7
        if money != 0:
            not_8 = child - successfull_8
            if money == 3 and not_8 == 1:
                successfull_8 -= 1
            if not_8 == 0:
                successfull_8 -= 1
        print(successfull_8)
    else:
        print(-1)


distribute(int(input()), int(input()))
