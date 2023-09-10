"""Muddled Menu"""


def get_menu(dish):
    """Do as <e>judge says"""
    menu_list = []
    while dish != "DONE":
        if dish == "SOMETHING'S WRONG":
            menu_list.clear()
        elif "Can't do:" in dish:
            pos = dish.find(":") + 2
            menu_list.remove(dish[pos:])
        elif dish == "CLOSED":
            menu_list.clear()
            break
        else:
            pos = dish.find("#")
            if dish[pos + 1:].isdigit():
                menu_list.insert(int(dish[pos + 1:]) - 1, dish[:pos - 1])
            else:
                menu_list.append(dish[:pos - 1])
        dish = str(input())
    menu_list_reverse = menu_list.copy()
    menu_list_reverse.reverse()
    print("Full Course: {} Reversed: {}".format(menu_list, menu_list_reverse))


get_menu(str(input()))
