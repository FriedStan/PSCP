"""Run Length Decoding"""


def decoder(code):
    """Decode the code"""
    text = ""
    num = ""
    for i in range(len(code)):
        if code[i].isdigit():
            num += code[i]
        else:
            text += int(num) * code[i]
            num = ""
    return text


print(decoder(str(input())))
