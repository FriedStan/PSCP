"""Median"""


def median(n_count):
    """Find the median"""
    population = []
    for _ in range(n_count):
        population.append(int(input()))
    population.sort()
    size = len(population)
    if size % 2 == 1:
        med = population[size // 2]
    else:
        med = population[(size // 2) - 1] + population[size // 2]
        med /= 2
    print("{:.1f}".format(med))


median(int(input()))
