"""[Midterm 2022] Netflix"""


def get_input():
    """Get all user input"""
    screen = int(input())
    user = int(input())
    inf_mov = str(input())
    mobile_use = str(input())
    laptop = str(input())
    hd_res = str(input())
    ultra_hd = str(input())
    return screen, user, inf_mov, mobile_use, laptop, hd_res, ultra_hd


def premium(screen, user, max_user, max_screen, total):
    """Do the premium package"""
    sub_premium = max(user // 4, screen // 4, 1)
    if user - (sub_premium * 4) >= 3 or screen - (sub_premium * 4) >= 3:
        sub_premium += 1
    max_user += sub_premium * 4
    max_screen += sub_premium * 4
    total += sub_premium * 419
    requirement_met = max_user >= user and max_screen >= screen
    print("Premium x {}".format(sub_premium))
    return total, requirement_met, sub_premium


def standard(screen, user, max_user, max_screen, total):
    """Do the premium package"""
    sub_standard = max(user // 2, screen // 2, 1)
    max_user += sub_standard * 2
    max_screen += sub_standard * 2
    total += sub_standard * 349
    requirement_met = max_user >= user and max_screen >= screen
    print("Standard x {}".format(sub_standard))
    return total, requirement_met, sub_standard


def basic(screen, user, max_user, max_screen, total):
    """Do the premium package"""
    sub_basic = max(user, screen, 1)
    max_user += sub_basic
    max_screen += sub_basic
    total += sub_basic * 279
    requirement_met = max_user >= user and max_screen >= screen
    print("Basic x {}".format(sub_basic))
    return total, requirement_met, sub_basic


def mobile(screen, user, max_user, max_screen, total):
    """Do the premium package"""
    sub_mobile = max(user, screen, 1)
    max_user += sub_mobile
    max_screen += sub_mobile
    total += sub_mobile * 99
    requirement_met = max_user >= user and max_screen >= screen
    print("Mobile x {}".format(sub_mobile))
    return total, requirement_met, sub_mobile


def netflix():
    """Suggest you a Netflix's subscription"""
    screen, user, inf_mov, mobile_use, laptop, hd_res, ultra_hd = get_input()
    total = 0
    max_user = bool(inf_mov) * 0
    max_screen = bool(mobile_use) * 0
    requirement_met = max_user >= user and max_screen >= screen
    if ultra_hd == "Yes" and not requirement_met or \
        (max(screen, user) >= 3 and "Yes" in (laptop, hd_res, ultra_hd)):
        total, requirement_met, sub_premium = premium(screen, user, max_user, max_screen, total)
        user -= sub_premium * 4
        screen -= sub_premium * 4
    if hd_res == "Yes" and not requirement_met or \
        (max(screen, user) == 2 and "Yes" in (laptop, hd_res)):
        total, requirement_met, sub_standard = standard(screen, user, max_user, max_screen, total)
        user -= sub_standard * 2
        screen -= sub_standard * 2
    if laptop == "Yes" and not requirement_met:
        total, requirement_met, sub_basic = basic(screen, user, max_user, max_screen, total)
        user -= sub_basic
        screen -= sub_basic
    if not requirement_met:
        total, requirement_met, sub_basic = mobile(screen, user, max_user, max_screen, total)
    print("Total = {} THB".format(total))


netflix()
