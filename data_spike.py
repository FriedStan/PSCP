"""DataSpike"""


def comparator(num_big, count):
    """Compare data"""
    if count < 8:
        num_inp = int(input())
        if num_big < num_inp:
            num_big = num_inp
            count += 1
            comparator(num_big, count)
        else:
            count += 1
            comparator(num_big, count)
    else:
        print(num_big)


def main():
    """Main func"""
    comparator(0, 0)


main()
