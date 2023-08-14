<<<<<<< HEAD
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
=======
"""BlackJack"""


def blackjacktifyer(this_hand):
    """Calculate blackjack's points"""
    total = 0
    a_count = 0
    for card in this_hand:
        if card.isdecimal():
            total += int(card)
        elif card.lower() in "jqk":
            total += 10
        elif card.lower() == "a":
            total += 1
            a_count += 1
        else:
            pass
>>>>>>> 9bf373e (add more files)
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
<<<<<<< HEAD
    total = 0
    while hand_size != 0:
        card = str(input())
        total += blackjacktifyer(card)
        hand_size -= 1
=======
    hand_card = []
    while hand_size != 0:
        card = str(input())
        hand_card.append(card)
        hand_size -= 1
    total = blackjacktifyer(hand_card)
>>>>>>> 9bf373e (add more files)
    return print(total)


main()
