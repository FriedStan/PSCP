"""ValidVar"""


def var_checker(text):
    """Check the var Is it valid?"""
    output = "Valid"
    if text[0].isdigit():
        output = "Invalid"
    elif text in ("if", "else", "elif", "while", "for", "True", "False", "continue", "break"\
                 , "return", "is", "in", "and", "or", "from", "as", "pass", "not", "def", "None"):
        output = "Invalid"
    else:
        for char in text:
            if char in "!\"#$%&'()*+, -./:;<=>?@[\\]^`{|}~":
                output = "Invalid"
    print(output)


def loop_input(loop_round):
    """Loop input"""
    for _ in range(loop_round):
        var_checker(str(input()).strip())


loop_input(int(input()))
