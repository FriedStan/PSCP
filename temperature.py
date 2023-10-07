"""Temperature"""


def converter(temp_pt, from_this, to_that):
    """Converter"""
    celcius_dict = {"C": temp_pt,
                    "F": (temp_pt - 32) * (5 / 9),
                    "K": temp_pt - 273.15,
                    "R": (temp_pt * (5 / 9)) - 273.15}
    celcius = celcius_dict.get(from_this)
    to_that_dict = {"C": celcius,
                    "F": (celcius * (9 / 5)) + 32,
                    "K": celcius + 273.15,
                    "R": (celcius + 273.15) * (9 / 5)}
    print("{:.2f}".format(to_that_dict.get(to_that)))


converter(float(input()), str(input()), str(input()))
