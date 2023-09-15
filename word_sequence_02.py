"""WordSequence II"""


def word_seq(text, target):
    """Slowly transform text"""
    transform = [*text]
    for num in range(max(len(target), len(text))):
        print(*transform, sep="")
        if num < min(len(target), len(text)):
            transform[num] = target[num]
        elif len(transform) > len(target):
            transform.pop(len(target))
        else:
            transform.append(target[num])
    print(*transform, sep="")


word_seq(str(input()), str(input()))
