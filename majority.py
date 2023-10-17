"""Majority"""


def major_minor(candidate, population):
    """Counting stars"""
    candidate_dict = dict((i, 0) for i in range(1, candidate + 1))
    for _ in range(population):
        candidate_dict[int(input())] += 1
    winner_score = sorted(candidate_dict.values(), reverse=True)[0]
    swap_score = dict((k, j) for j, k in candidate_dict.items())
    print("{} {}".format(swap_score.get(winner_score), winner_score)\
          if winner_score > population / 2 else "0 {}".format(winner_score))


major_minor(int(input()), int(input()))
