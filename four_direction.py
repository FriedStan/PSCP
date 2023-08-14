"""FourDirections"""


def left_arrow(row):
    """Make up arrow"""
    if row == 0:
        text = "  *  "
    elif row == 1:
        text = " *   "
    elif row == 2:
        text = "*****"
    elif row == 3:
        text = " *   "
    elif row == 4:
        text = "  *  "
    return text


def right_arrow(row):
    """Make up arrow"""
    if row == 0:
        text = "  *  "
    elif row == 1:
        text = "   * "
    elif row == 2:
        text = "*****"
    elif row == 3:
        text = "   * "
    elif row == 4:
        text = "  *  "
    return text


def up_arrow(row):
    """Make up arrow"""
    if row == 0:
        text = "  *  "
    elif row == 1:
        text = " *** "
    elif row == 2:
        text = "* * *"
    elif row == 3:
        text = "  *  "
    elif row == 4:
        text = "  *  "
    return text


def down_arrow(row):
    """Make up arrow"""
    if row == 0:
        text = "  *  "
    elif row == 1:
        text = "  *  "
    elif row == 2:
        text = "* * *"
    elif row == 3:
        text = " *** "
    elif row == 4:
        text = "  *  "
    return text


def four_arrow(seq):
    """Point arrow"""
    text = ""
    for row in range(5):
        for char in seq:
            if char == "U":
                text += up_arrow(row)
            elif char == "D":
                text += down_arrow(row)
            elif char == "L":
                text += left_arrow(row)
            elif char == "R":
                text += right_arrow(row)
            text += " "
        text += "\n"
    print(text)


four_arrow(str(input()).upper())
