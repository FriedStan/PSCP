"""LineSorting"""


def main(num):
    """LineSorting"""
    text_list = []
    for _ in range(num):
        text_list.append(input())
    text_list.sort(key=len)
    for i in text_list:
        print(i)


main(int(input()))
