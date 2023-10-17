"""Discount"""


def book_discounter(book):
    """5 get 1 free"""
    cart = []
    while book != "ENTER":
        cart.append(int(book))
        book = str(input())
    book_count = len(cart)
    free_book = book_count // 6
    print(book_count)
    print(free_book)


book_discounter(str(input()))
