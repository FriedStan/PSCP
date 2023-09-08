"""LastStand"""
import json


def main(text):
    """LastStand"""
    text_list = json.loads(text)
    for i in text_list:
        i = int(i)
        last = i % 10
        print(last)


main(input())
