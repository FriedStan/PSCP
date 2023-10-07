"""Dart"""
from math import sqrt


def is_it_in(point):
    """Find that point in circle"""
    distance_from_0 = sqrt((next(point) ** 2) + (next(point) ** 2))
    return distance_from_0


def score_counter(dart):
    """Count the score of each dart"""
    total_score = 0
    for _ in range(dart):
        distance = is_it_in(map(int, str(input()).split()))
        for i in range(2, 12, 2):
            if i - 2 <= distance <= i:
                total_score += 5 - ((i - 2) / 2)
                break
    print(int(total_score))


score_counter(int(input()))
