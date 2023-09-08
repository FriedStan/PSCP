"""MissingCard"""


def build_deck():
    """Build 52 deck"""
    rank = "23456789TJQKA"
    face = "SHDC"
    card_deck = []
    for char in rank:
        for things in face:
            card_deck.append((char + things).replace("T", "10"))
    return set(card_deck)


def card_miss():
    """Find the missing card"""
    card_deck = build_deck()
    user_deck = set()
    for _ in range(51):
        user_deck.add(str(input()))
    print(list(card_deck.difference(user_deck))[0])


card_miss()
