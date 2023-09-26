"""CaesarV2"""


def decoder(text):
    """Decoder the text by shift value"""
    alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text_copied = text.copy()
    shift_value = 1
    while shift_value < 26:
        for i, char in enumerate(text):
            if char.isalpha():
                shift_to = (alphabeth.find(char.upper()) + shift_value) % 26
                if char.islower():
                    text_copied[i] = alphabeth[shift_to].lower()
                else:
                    text_copied[i] = alphabeth[shift_to]
        sentence = "".join(text_copied)
        if "the" in sentence.lower():
            break
        shift_value += 1
    print(sentence)


decoder(list(str(input())))
