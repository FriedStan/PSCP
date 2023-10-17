"""Digit v2"""


def digitifyer(text):
    """From text to digit"""
    if 'thousand' in text:
        digit = 4
    elif 'hundred' in text:
        digit = 3
    elif any(['ty' in text, 'ten' in text, 'eleven' in text, 'twelve' in text, 'teen' in text]):
        digit = 2
    else:
        digit = 1
    print(digit if text else "")


digitifyer(str(input()))
