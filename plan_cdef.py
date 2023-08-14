"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""


def comparator(user_inp, num_1, num_2, num_3):
    """Compare data"""
    if num_1 >= num_2 >= num_3:
        num_big, num_mid, num_small = num_1, num_2, num_3
    elif num_1 >= num_3 >= num_2:
        num_big, num_mid, num_small = num_1, num_3, num_2
    elif num_2 >= num_1 >= num_3:
        num_big, num_mid, num_small = num_2, num_1, num_3
    elif num_2 >= num_3 >= num_1:
        num_big, num_mid, num_small = num_2, num_3, num_1
    elif num_3 >= num_2 >= num_1:
        num_big, num_mid, num_small = num_3, num_2, num_1
    else:
        num_big, num_mid, num_small = num_3, num_1, num_2
    if user_inp == "Ascend":
        print("%.2f, %.2f, %.2f" %(num_small, num_mid, num_big))
    elif user_inp == "Descend":
        print("%.2f, %.2f, %.2f" %(num_big, num_mid, num_small))
    else:
        pass


def main():
    """Main func"""
    user_inp = str(input()).capitalize()
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    comparator(user_inp, num_1, num_2, num_3)


main()
