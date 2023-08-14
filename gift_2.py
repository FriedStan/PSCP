"""Gift 2"""


def find_even(gift_list, count):
    """Find even number in list"""
    if count < 8:
        if gift_list[count] % 2 == 0:
            print(gift_list[count])
        else:
            pass
        count += 1
        find_even(gift_list, count)
    else:
        pass


def list_maker(gift_list):
    """Make gift list"""
    if len(gift_list) < 8:
        gift_w = int(input())
        gift_list.append(gift_w)
        list_maker(gift_list)
    else:
        pass


def main():
    """Main func"""
    gift_list = []
    list_maker(gift_list)
    find_even(gift_list, 0)


main()
