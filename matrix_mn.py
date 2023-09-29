"""Matrix_MN"""


def matrix_maker(row, col):
    """Make a matrix"""
    past = []
    present = []
    for _ in range(row):
        for _ in range(col):
            past.append(int(input()))
        present.append(past.copy())
        past.clear()
    for things in present:
        print(*things)


matrix_maker(int(input()), int(input()))
