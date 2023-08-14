"""SaveComputeRepeat"""


def main():
    """Doc"""
    start_here = 492137954293754252786
    millisec = start_here
    sec = millisec // 1000
    millisec %= 1000
    minute = sec // 60
    sec %= 60
    hrs = minute // 60
    minute %= 60
    day = hrs // 24
    hrs %= 24
    print(day, hrs, minute, sec, millisec)


main()
