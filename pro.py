"""Pro"""


def three_for_four(come, pay, per_person, if_come):
    """จ่าย3มา4"""
    get_pro = if_come // come
    free_person = come - pay
    print((if_come - (get_pro * free_person)) * per_person)


three_for_four(int(input()), int(input()), int(input()), int(input()))
