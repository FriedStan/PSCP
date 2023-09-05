"""[Midterm 2023] Lift"""


def elevator(people, weight_treshold):
    """Tell ths the lift is safe or not"""
    age_safe = False
    for _ in range(people):
        current_age = int(input())
        current_weight = float(input())
        if current_age >= 12:
            age_safe = True
        weight_treshold -= current_weight
    if weight_treshold < 0 or (age_safe is False and people > 0):
        print("Not Safe")
    else:
        print("Safe")


elevator(int(input()), float(input()))
