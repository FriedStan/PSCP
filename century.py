"""[Midterm 2021 + Recommend] Century"""


def to_ad_converter(year):
    """Change BE to AD"""
    year = year.replace(" ", "")
    year_num = int(year[4:])
    if year[:4] == "B.E.":
        year_num -= 543
    return year_num


def centurion(that_much_year):
    """Change from AD/BE to Century"""
    for _ in range(that_much_year):
        year_num = to_ad_converter(str(input()))
        century = year_num // 100
        if century < 0:
            print("ERROR")
        else:
            print(century if year_num / 100 == century else century + 1)


centurion(int(input()))
