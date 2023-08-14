"""SurprisingVote"""


def store_review(review_high, review_left):
    """Surprising innit"""
    count = review_high
    review_lowest = review_left - count
    while review_lowest < 0:
        review_lowest = review_left - count
        count -= 1
    if review_high - review_lowest > 2:
        text = "Surprising"
    else:
        text = "Not surprising"
    return text


def main():
    """Main func"""
    review_sum = float(input())
    review_high = float(input())
    review_left = review_sum - review_high
    print(store_review(review_high, review_left))


main()
