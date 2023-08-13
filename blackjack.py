"""Blackjack"""


def blackjacktifyer(card):
    """Calculate blackjack's points"""
    total = 0
    a_count = 0
    if card.isdecimal():
        total += int(card)
    elif card.lower() in "jqk":
        total += 10
    elif card.lower() == "a":
        total += 1
        a_count += 1
    else:
        pass
    while a_count != 0:
        if total <= 21 and (total + 10) <= 21:
            total += 10
        else:
            pass
        a_count -= 1
    return total


def main():
    """Get cards list from user"""
    hand_size = int(input())
    total = 0
    while hand_size != 0:
        card = str(input())
        total += blackjacktifyer(card)
        hand_size -= 1
    return print(total)


main()
