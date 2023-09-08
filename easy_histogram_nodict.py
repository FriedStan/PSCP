"""Easy Histogram (No Dict)"""


def histogram(text):
    """Count the letter in text"""
    histolist_lower = []
    histolist_upper = []
    for char in text:
        if char.isalpha():
            if char not in histolist_lower and char.islower():
                histolist_lower.append(char)
            elif char not in histolist_upper and char.isupper():
                histolist_upper.append(char)
    histolist_lower.sort()
    histolist_upper.sort()
    for things in histolist_lower:
        print("{} = {}".format(things, text.count(things)))
        if things.upper() in histolist_upper:
            upper = things.upper()
            print("{} = {}".format(upper, text.count(upper)))


histogram(str(input()))
