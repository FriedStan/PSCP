"""MissingCard (No Set)"""


def build_deck():
    """Build 52 deck"""
    rank = "23456789TJQKA"
    face = "SHDC"
    card_deck = []
    for char in rank:
        for things in face:
            card_deck.append((char + things).replace("T", "10"))
    return card_deck


def card_miss():
    """Find the missing card"""
    card_deck = build_deck()
    user_deck = []
    for _ in range(51):
        user_deck.append(str(input()))
    for things in card_deck:
        if things not in user_deck:
            print(things)
            break


card_miss()
