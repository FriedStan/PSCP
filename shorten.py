"""[Midterm 2020] Shorten"""


def size_minimizer(current_size):
    """Minimize shirt size into range"""
    all_size = ""
    size_chart = ""
    while current_size != -1:
        all_size += str(current_size) + "|"
        current_size = int(input())
    chain = False
    first_digit = ""
    for things in all_size:
        if things.isdigit():
            first_digit += things
        else:
            break
    current_num = ""
    prev_num = 0
    if first_digit != "":
        prev_num = int(first_digit)
    for things in all_size:
        if things.isdigit():
            current_num += things
        else:
            if current_num == first_digit:
                size_chart = first_digit
            elif int(current_num) - prev_num == 1 and chain is False:
                size_chart += "-" + current_num
                chain = True
            elif int(current_num) - prev_num == 1 and chain is True:
                size_chart = size_chart.replace(str(prev_num), current_num)
            else:
                size_chart += ", " + current_num
                chain = False
            prev_num = int(current_num)
            current_num = ""
    print(size_chart)


size_minimizer(int(input()))
