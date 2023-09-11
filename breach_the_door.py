"""Breach the Door"""


def breacher(text):
    """Make the password use <e>judge method"""
    all_text = text.split()
    use_text = []
    for things in all_text:
        for char in things:
            if not char.isalnum() or char.isdigit():
                things = things.replace(char, "")
        size = len(things)
        if size > 6:
            use_text.append(things)
    print(" ".join(use_text))


breacher(str(input()))
