"""Hon Bun Jung"""
from math import ceil


def hong_salary(day):
    """1hr/ 8720 Won"""
    hour = 0
    for _ in range(day):
        hour += ceil(float(input()))
    print(hour * 8720)


hong_salary(int(input()))
