"""MissingCard (No Set)"""


def build_deck():
    """Build 52 deck"""
    rank = "23456789TJQKA"
    face = "SHDC"
    card_deck = []
    for char in rank:
        for things in face:
            if char == "T":
                card_deck.append("10" + things)
            else:
                card_deck.append(char + things)
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
