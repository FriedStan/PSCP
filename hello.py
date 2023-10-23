"""Helloooo"""


def hello_hi(text):
    """Helloooo"""
    text_reversed = text[::-1]
    count = 0
    for i in text_reversed:
        if i in "aeiou":
            break
        count += 1
    try:
        vowel = text_reversed[count]
        actual_text = (text_reversed[:count] + (vowel * 3) + text_reversed[count:])[::-1]
    except IndexError:
        actual_text = text
    print(actual_text)


hello_hi(str(input()))
