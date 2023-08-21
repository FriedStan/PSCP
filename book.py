"""[Midterm 2020] Books"""
from math import ceil


def booktifyer(books, pages, x_pt, y_pt):
    """อ่านหนังสือกันครับ"""
    day_used = 0
    prev_read = 0
    book_left = books
    read = 0
    for _ in range(books):
        current_day = 0
        book_pages = pages
        while book_pages > 0 and read < pages:
            read = ceil(((x_pt + current_day + prev_read) / \
                    (y_pt + current_day + prev_read)) * pages)
            book_pages -= read
            current_day += 1
            day_used += 1
        book_left -= 1
        if read >= pages:
            break
        prev_read += current_day
    print(day_used + book_left)


booktifyer(int(input()), int(input()), int(input()), int(input()))
