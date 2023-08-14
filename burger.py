"""Let's make Hamubaga!!!"""


def burgertifyer():
    """Make hamubaga"""
    top_bun = int(input())
    bot_bun = int(input())
    patty_size = (top_bun + bot_bun) * 2
    print("|" * top_bun + "*" * patty_size + "|" * bot_bun)


burgertifyer()
