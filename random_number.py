"""Doc"""
import random


def main():
    """Doc"""
    user_inp = int(input())
    this_list = []
    for _ in range(user_inp * 2):
        num = random.randrange(10000, 100000)
        print(num, end=" ")
        this_list.append(num)
    #print()
    this_list.sort()
    #print(this_list)


main()
