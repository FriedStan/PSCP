"""3nPlus1"""


def counter(num):
    """Count the times that num has been interact until num is 1"""
    out_put = []
    count = 1
    num_mirror = num
    while num != 0:
        if num_mirror % 2 == 0:
            num_mirror /= 2
            count += 1
        elif num_mirror == 1:
            num = int(input())
            out_put.append(count)
            num_mirror = num
            count = 1
        else:
            num_mirror = (num_mirror * 3) + 1
            count += 1
    print(*out_put, sep="\n")


counter(int(input()))
