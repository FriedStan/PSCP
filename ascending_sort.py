"""AscendingSort"""


def sorter():
    """Sort the number in ascending"""
    num_list = []
    for _ in range(5):
        num_list.append(int(input()))
    num_list.sort()
    for i in range(5):
        print(num_list[i])


sorter()
