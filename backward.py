"""Backward"""


def backwarder(text):
    """Do a flip"""
    text_list = []
    while text != "NULL":
        text_list.append(text)
        text = str(input())
    text_list.reverse()
    for things in text_list:
        print(things)


backwarder(str(input()))
