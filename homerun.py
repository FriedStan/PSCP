"""[Midterm 2023] Home Run"""


def home_runner(hits, player_power):
    """Calculate homerun"""
    count = 0
    for _ in range(hits):
        base_length = float(input())
        if base_length < player_power:
            count += 1
    print(count)


home_runner(int(input()), float(input()))
