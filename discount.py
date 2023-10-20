"""Discount"""


def book_discounter(book):
    """5 get 1 free"""
    cart = []
    while book != "ENTER":
        cart.append(int(book))
        book = str(input())
    book_count = len(cart)
    free_book = book_count // 5 if book_count != 5 else 0
    if free_book == 3:
        free_book -= 1
    print(sum(sorted(cart)[free_book:]))


book_discounter(str(input()))
