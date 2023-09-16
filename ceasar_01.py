"""CaesarV1"""


def decoder(shift_value, text):
    """Decoder the text by shift value"""
    alphabeth = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    text = list(text)
    for i, char in enumerate(text):
        if char.isalpha():
            shift_to = (alphabeth.index(char.upper()) + shift_value) % 26
            if char.islower():
                text[i] = alphabeth[shift_to].lower()
            else:
                text[i] = alphabeth[shift_to]
    print(*text, sep="")


decoder(int(input()), str(input()))
