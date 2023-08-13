"""FourDirections"""


def up_down_arrow(row, direction):
    """Make up arrow"""
    if direction == "U":
        if row == 0:
            text = "  *  "
        elif row == 1:
            text = " *** "
        elif row == 2:
            pass


def four_arrow(seq):
    """Point arrow"""
    text = ""
    for row in range(5):
        for _ in range(len(seq)):
            count = 0
            for char in seq:
                if char in ("U", "D"):
                    if row in (0, 3, 4):
                        text += "*"
                else:
                    text += " "
                count += 1
        text += "\n"
    print(text)


four_arrow(str(input()).upper())
