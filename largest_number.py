"""Largest Number"""


def comparator(value_list, num_big, count):
    """Compare the value to find the biggest"""
    if count < 6:
        if num_big < value_list[count]:
            num_big = value_list[count]
        else:
            pass
        count += 1
        comparator(value_list, num_big, count)
    else:
        print(num_big)


def arranger(num_1, num_2, num_3):
    """Arrange number"""
    value_1 = int(num_1 + num_2 + num_3)
    value_2 = int(num_1 + num_3 + num_2)
    value_3 = int(num_2 + num_1 + num_3)
    value_4 = int(num_2 + num_3 + num_1)
    value_5 = int(num_3 + num_2 + num_1)
    value_6 = int(num_3 + num_1 + num_2)
    value_list = [value_1, value_2, value_3, value_4, value_5, value_6]
    comparator(value_list, 0, 0)


def main():
    """Main func"""
    num_1 = str(input())
    num_2 = str(input())
    num_3 = str(input())
    arranger(num_1, num_2, num_3)


main()
