"""Easy Histogram"""


def histogram(text):
    """Do as <e>judge says"""
    text_list = []
    text_dict = {}
    for char in text:
        if char not in text_list and char.isalpha():
            text_list.append(char.lower())
    text_list.sort()
    for char in text_list:
        if char.lower() not in text_dict and char.isalpha():
            text_dict.update({char.lower(): [char.lower(), char.upper()]})
    for _, alpha in text_dict.items():
        if text.count(alpha[0]) >= 1:
            print("{} = {}".format(alpha[0], text.count(alpha[0])))
        if text.count(alpha[1]) >= 1:
            print("{} = {}".format(alpha[1], text.count(alpha[1])))


histogram(str(input()))
