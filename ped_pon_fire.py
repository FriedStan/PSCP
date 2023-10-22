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
        if (i, need) not in hof:
            if side_a == side_b and side_a != 0 and side_b != 0 and i == need:
                for i in range(1, side_a):
                    paired += i
                hof.update({(need, i): '', (i, need): ''})
            elif i in coop and need in coop:
                paired += side_a * side_b
                hof.update({(need, i): '', (i, need): ''})
    print(paired)


this_is_a_pong(int(input()))
