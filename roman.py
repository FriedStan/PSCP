"""Roman number"""


def roman_to_decimal(roman_num):
    """Roman to Decimal number"""
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    prev_num = roman_dict[roman_num[0]] + 1
    num = 0
    for char in roman_num:
        current_num = roman_dict[char]
        if prev_num < current_num:
            num += current_num - (prev_num * 2)
        else:
            num += current_num
        prev_num = current_num
    print(num)


roman_to_decimal(str(input()).upper())
