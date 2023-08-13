"""Runner"""


def text_loop_v2(text, times):
    """Print text for times times"""
    for _ in range(times):
        print(text)


text_loop_v2(input(), int(input()))
