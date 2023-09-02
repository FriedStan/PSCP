"""Gotta catch them all"""
from math import ceil


def ryu_sei_ken(punch_count, times):
    """ペガサス流星拳, Pegasasu Ryu Sei Ken 165p per sec"""
    return punch_count + (165 * times)


def sui_sei_ken(punch_count, times):
    """ペガサス彗星拳, Pegasasu Sui Sei Ken"""
    return punch_count + (1 * times)


def rolling_crash(punch_count, times):
    """ペガサスローリングクラッシュ, Pegasasu Rolling Crash"""
    return punch_count + (12 * times)


def begin_punch(sec, punch):
    """T4E"""
    sui_ken = int(int(punch / 165) / 2)
    ryu_ken = ceil((punch - sui_ken) / 165)
    if ceil(int(punch - (ryu_ken * 165)) / 2) >= 0 or sui_ken > int(sec /6):
        print(1)
        if sui_ken > int(sec /6):
            sui_ken = int(sec / 6)
            print("1_1")
        elif ceil(int(punch - (ryu_ken * 165)) / 2) == 0:
            sui_ken -= 1
            print("1_3")
        else:
            sui_ken = ceil(int(punch - (ryu_ken * 165)) / 2)
            print("1_2")
    if ryu_ken > int(sec / 2) - int(sec / 6):
        ryu_ken = int(sec / 2) - int(sec / 6)
    roll_ken = sec - ((ryu_ken * 2) + (sui_ken * 2) + 1)
    if roll_ken < 0 or roll_ken > sec:
        roll_ken = 0
    attack = 0
    attack = ryu_sei_ken(attack, ryu_ken)
    attack = sui_sei_ken(attack, sui_ken)
    attack = rolling_crash(attack, roll_ken)
    print("Ryu", ryu_ken)
    print("Sui", sui_ken)
    print("Roll", roll_ken)
    print(attack)
    print()


def saint_loop(sec, punch):
    """Loop"""
    attack = 0
    current_sec = 1
    ryu_ken = 0
    sui_ken = 0
    roll_ken = 0
    while attack < punch and current_sec <= sec:
        if current_sec % 6 == 0:
            attack = sui_sei_ken(attack, 1)
            sui_ken += 1
        elif current_sec % 2 == 0:
            attack = ryu_sei_ken(attack, 1)
            ryu_ken += 1
        current_sec += 1
    if current_sec < sec:
        attack = rolling_crash(attack, sec - current_sec)
        roll_ken = sec - current_sec
    print("Ryu", ryu_ken)
    print("Sui", sui_ken)
    print("Roll", roll_ken)
    print(attack)


num1 = int(input())
num2 = int(input())
#int(input()), int(input())
begin_punch(num1, num2)
saint_loop(num1, num2)
