"""[Midterm 2021] B - Fully pair?"""


def pairing(text):
    """Return fully paired if they're all fully pair otherwise return the unpaired character"""
    out = ""
    for char in text:
        if text.count(char) % 2 == 1:
            if char not in out:
                out += char
    if out == "":
        out = "fully paired"
    print(out)


pairing(str(input()))
