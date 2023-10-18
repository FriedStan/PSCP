"""PedPonFire"""


def this_is_a_pong(ducks):
    """Duck duck go"""
    coop = {}
    hof = {}
    paired = 0
    for _ in range(ducks):
        current_duck = int(input())
        coop[current_duck] = coop.get(current_duck, 0) + 1
    target = int(input())
    for i in coop:
        need = target - i
        side_a = coop.get(need, 0)
        side_b = coop.get(i, 0)
        if (i, need) not in hof and (need != i or side_a > 1 or side_b > 1) and need in coop:
            paired += side_a * side_b
            hof.update({(need, i): '', (i, need): ''})
    print(paired)


this_is_a_pong(int(input()))
