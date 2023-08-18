"""Big Frame"""


def framing():
    """Frame the text"""
    text_1 = str(input()).strip()
    text_2 = str(input()).strip()
    text_3 = str(input()).strip()
    text_4 = str(input()).strip()
    text_5 = str(input()).strip()
    text_t4e = [text_1, text_2, text_3, text_4, text_5]
    frame_size = max(len(text_1), len(text_2), len(text_3), len(text_4), len(text_5))
    print("*" * (frame_size + 4))
    for text in text_t4e:
        print("* " + text + " " * (frame_size - len(text))+ " *")
    print("*" * (frame_size + 4))


framing()
