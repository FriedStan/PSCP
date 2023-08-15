"""BlackJack"""


def blackjacktifyer(hand):
    """Count blackjack score"""
    score = 0
    for card in hand:
        if card in "TJQK":
            score += 10
        elif card.isdigit():
            score += int(card)
        else:
            pass
    for i in range(hand.count("A")):
        score += 1
        if score + 10 <= 21 and i == hand.count("A") - 1:
            score += 10
    return score


def get_card(size):
    """Get card"""
    hand = ""
    for _ in range(size):
        card = str(input()).upper()
        if card == "10":
            hand += "T"
        else:
            hand += card
    return hand


def main():
    """Main func"""
    hand = get_card(int(input()))
    print(blackjacktifyer(hand))


main()
