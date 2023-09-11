"""LetterFrequency"""


def use_most(text):
    """Find the most use alphabet"""
    alphabet_list = []
    alphause_list = []
    most_use_dict = {}
    for char in text:
        if char.isalpha() and char not in alphabet_list:
            alphabet_list.append(char)
            alphause_list.append(text.count(char))
            most_use_dict.update({text.count(char): char})
    alphause_list.sort()
    print(most_use_dict[alphause_list[len(alphause_list) - 1]])


use_most(str(input()))
