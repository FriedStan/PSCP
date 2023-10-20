"""113"""


def one_one_three(text):
    """113 -> Nothing"""
    while '113' in text:
        text = text.replace("113", "")
    print(text)


one_one_three(str(input()))
