"""asd"""
TEXT = [1, 2, 3]

def printin():
    """asd"""
    global TEXT
    print(TEXT)
    TEXT.append(15)
    print(TEXT)
    TEXT = [1, 3, 4]
    print(TEXT)


printin()
