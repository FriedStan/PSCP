"""Sequence XXX"""


def sequencer_30(size, amount):
    """Do as <e>judge says"""
    text = ""
    for row in range(size):
        for _ in range(amount):
            count = 0
            for col in range(size):
                if row in (0, col, size - 1, size - col - 1) or count in (0, size - 1):
                    text += "*"
                else:
                    text += " "
                count += 1
            text += " "
        text += "\n"
    print(text)

sequencer_30(int(input()), int(input()))
