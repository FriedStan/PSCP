"""Easy Histogram"""


def histogram(text):
    """Do as <e>judge says"""
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict.update({char: 1})
        else:
            char_dict[char] += 1
    sorted_dict = sorted(char_dict, key=lambda x: (x.lower(), x.swapcase()))
    for things in sorted_dict:
        print("{} = {}".format(things, char_dict.get(things)))


histogram(str(input()).replace(" ", ""))
