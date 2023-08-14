"""Docstring"""


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



def weight_compare(weight_list, duo):
    """Compare weight for the good sake of kayak"""
    diff_sum = 0
    #loop = 1
    #print(weight_list)
    #print("Duo start:", duo, "\n")
    while len(weight_list) > 2 and duo > 0:
        #print("Loop %d:" % loop, weight_list)
        #loop += 1
        pos_1 = weight_list[0]
        pos_2 = weight_list[1]
        pos_3 = weight_list[2]
        diff_1 = pos_2 - pos_1
        diff_2 = pos_3 - pos_2

        if len(weight_list) > 3:
            pos_4 = weight_list[3]
            diff_3 = pos_4 - pos_3
        else:
            diff_3 = diff_2 + 1

        if diff_1 <= diff_2 and diff_1 <= diff_3:
            #print("Add diff 1:", diff_1)
            diff_sum += diff_1
            del weight_list[0:2]
            duo -= 1
        elif diff_3 <= diff_2 and diff_3 <= diff_1:
            #print("Add diff 3:",diff_3)
            diff_sum += diff_3
            del weight_list[2:4]
            duo -= 1
        else:
            #print("Add diff 2:",diff_2)
            diff_sum += diff_2
            del weight_list[1:3]
            duo -= 1

        #print("Left:", weight_list)
        #print("Duo left:", duo, "\n")
    print(diff_sum)


def get_input():
    """User input weight"""
    that_n = int(input())
    weight = str(input())
    weight_list = list(map(int, weight.split()))
    weight_list.sort()
    return weight_list, that_n


def main():
    """Main Function"""
    weight_list, this_n = get_input()
    duo = this_n - 1
    #print(weight_list)
    weight_list, duo = duo_kayak(weight_list, duo)
    weight_compare(weight_list, duo)


main()
