"""Second Converter"""


def inception():
    """Do as <e>judge says"""
    k_sec = int(input())
    one_min = int(input())# 1-min = input sec
    one_hour = int(input())# 1-hour = input min
    one_day = int(input()) # 1-day = input hour
    minute = k_sec // one_min
    sec = k_sec % one_min
    hour = minute // one_hour
    minute = minute % one_hour
    hour = hour % one_day
    print("{:d}:{:d}:{:d}".format(hour, minute, sec))


inception()
