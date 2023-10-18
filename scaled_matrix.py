"""ScaledMatrix"""


def matrix_scaler(row, col):
    """Met trick"""
    unscale = [float(input()) for _ in range(col * row)]
    maxine = max(unscale)
    minna = min(unscale)
    scaled = map(lambda i: "{:.2f}".format((i - minna) / (maxine - minna)), unscale)
    for _ in range(row):
        for _ in range(col):
            print(next(scaled), end=" ")
        print()


matrix_scaler(int(input()), int(input()))
