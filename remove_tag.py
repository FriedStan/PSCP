"""RemoveTag"""


def tag_remover(text):
    """Remove HTML tag"""
    text_list = []
    if "<" in text or ">" in text:
        for _ in range(text.count("<")):
            text = text[text.find(">") + 1:]
            text_list.append(text[:text.find("<")].strip())
            text = text[text.find("<") + 1:]
    else:
        text_list = text.split()
    print(" ".join(text_list).split())


tag_remover(str(input()))
