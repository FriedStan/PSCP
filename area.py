"""Area"""


def in_your_area(line):
    """LIATE"""
    shape = [input().strip().replace(" ", "") for _ in range(line)]
    print(sum(len(i) for i in shape))


in_your_area(int(input()))
