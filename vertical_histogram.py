"""VerticalHistogram"""


def horizon_zerodawn(text):
    """Make a graph"""
    text_list = list(map(str.swapcase, sorted(set(list(text.swapcase())))))
    text_count = [text.count(i) for i in text_list]
    count = max(text_count)
    for _ in range(count):
        print("{:03d} ".format(count), end="")
        for num in text_count:
            if count <= num:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        count -= 1
        print()
    print("   ", *text_list, sep=" ")


horizon_zerodawn(str(input()))
