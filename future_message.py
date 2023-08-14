"""Future Message"""


def text_checker(text=str):
    """Check the text that user input"""
    if text.isdecimal():
        result = "Number"
    elif text.isupper():
        result = "Uppercase"
    elif text.islower():
        result = "Lowercase"
    elif text.istitle():
        result = "Title"
    elif text.isspace():
        result = "Space"
    else:
        result = "Other"
    return result


print(text_checker(str(input())))
