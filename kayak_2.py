"""Docstring"""


def checker(real_kayak, duo):
    """Get fish"""
    check_list = []
    diff_sum = 0
    for pair in real_kayak:
        person_1, person_2 = pair
        if person_1 not in check_list and person_2 not in check_list:
            check_list.append(person_1)
            check_list.append(person_2)
            if duo > 0:
                diff_sum += person_1 - person_2
                duo -= 1
    print(check_list)
    print("Kayak:", real_kayak)
    print(diff_sum)


def duo_kayak(weight_list, duo):
    """Put people into the duo kayak"""
    for people in weight_list:
        quantity = weight_list.count(people)

        if quantity % 2 == 0:
            duo -= quantity // 2
            while quantity != 0:
                weight_list.remove(people)
                quantity -= 1
        else:
            duo -= quantity // 2
            while quantity != 1:
                weight_list.remove(people)
                quantity -= 1

    return weight_list, duo


def comparator(weight_list, duo):
    """Compare weight"""
    size = len(weight_list)
    compare_list = []
    for i in range(size - 1):
        mem = weight_list[i] - weight_list[i + 1]
        compare_list.append(mem)
    compare_sort = compare_list.copy()
    compare_sort.sort()
    real_kayak = []
    print("Duo start:", duo)
    print(weight_list)
    print("List:", compare_list)
    print("Sort:", compare_sort)
    for thing in compare_sort:
        if thing in compare_list and len(compare_sort) > duo:
            pos_del = compare_list.index(thing)
            compare_list.pop(pos_del)
            compare_list.insert(pos_del, -1)
            real_kayak.append((weight_list[pos_del], weight_list[pos_del + 1]))
        else:
            pass
    return real_kayak, duo


def get_input():
    """User input weight"""
    that_n = int(input())
    weight = str(input())
    weight_list = list(map(int, weight.split()))
    weight_list.sort(reverse=True)
    return weight_list, that_n


def main():
    """Main Function"""
    weight_list, this_n = get_input()
    duo = this_n - 1
    weight_list, duo = duo_kayak(weight_list, duo)
    real_kayak, duo = comparator(weight_list, duo)
    checker(real_kayak, duo)


main()
