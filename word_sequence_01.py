"""WordSequence I"""


def word_sequencer(text):
    """Print text in sequence"""
    for i in range(len(text)):
        print(text[:i + 1])


word_sequencer(str(input()))
