"""ฉันจะเป็น Saitama ให้ได้เลย"""
from math import ceil


def my_mc(num_1, num_2):
    """My own max"""
    return num_1 if num_1 >= num_2 else num_2


def saitama_workout():
    """Saitama workout"""
    push_up = int(input())
    sit_up = int(input())
    squat = int(input())
    run = int(input())
    push_day = ceil(push_up / int(input()))
    sit_day = ceil(sit_up / int(input()))
    run_day = ceil(run / int(input()))
    squat_day = ceil(squat / int(input()))
    all_workout = "{},{},{},{}".format(push_day, sit_day, squat_day, run_day)
    biggest = 0
    number = ""
    for things in all_workout:
        if things.isdigit():
            number += things
        else:
            biggest = my_mc(int(number), biggest)
            number = ""
    print(biggest)


saitama_workout()
