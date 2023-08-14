"""Day 1"""


def leap_year(year):
    """Tell that you input leap year or not"""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = "Yes"
    else:
        leap = "No"
    return leap


def main():
    """Main func"""
    year_inp = int(input())
    print(leap_year(year_inp))


main()
