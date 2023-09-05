"""[Midterm 2023] Bonus"""


def bonus_calc(current_income, year_work, month_work):
    """Calculate the bonus"""
    if month_work >= 10:
        year_work += 1
    year_work = min(20, year_work)
    bonus = min(max(current_income * year_work, 5000), 1000000)
    return bonus


print(bonus_calc(int(input()), int(input()), int(input())))
