"""[Midterm 2023] Bad Keyboard"""


def keyboard_fixer(text):
    """Fix the keyboard"""
    new_text = ""
    for char in text:
        if char == "i":
            new_text += "o"
        elif char == "o":
            new_text += "i"
        elif char == "I":
            new_text += "O"
        elif char == "O":
            new_text += "I"
        else:
            new_text += char
    print(new_text)


keyboard_fixer(str(input()))
