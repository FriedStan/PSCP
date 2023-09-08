"""MissingNumber (No Set)"""


def missing_num(num_range):
    """Find the missing number"""
    num_list = []
    missing = []
    num = int(input())
    while num != 0:
        num_list.append(num)
        num = int(input())
    for num in range(1, num_range + 1):
        if num not in num_list:
            missing.append(num)
    missing.sort()
    for things in missing:
        print(things)


missing_num(int(input()))
