"""https://open.spotify.com/intl-ja/track/3LzQ0QF4Ud7CyAIWdFxUHl?si=3ba687420e964150"""
from math import sqrt, ceil


def inkinator(speed_request):
    """Tell you when will the ink reach you"""
    speed_request = list(map(int, speed_request.split()))
    p_i = 3.1416
    out_put = []
    for _ in range(speed_request[1]):
        village_pos = list(map(int, str(input()).split()))
        distance_from_0 = sqrt(village_pos[0] ** 2 + village_pos[1] ** 2)
        time = (distance_from_0 ** 2) * (p_i / speed_request[0])
        out_put.append(ceil(time))
    print(*out_put, sep="\n")


inkinator(str(input()))
