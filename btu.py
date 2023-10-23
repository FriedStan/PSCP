"""BTU"""


def btu_calc(room_area):
    """Room -> BTU"""
    if room_area in range(100, 151):
        btu = 5000
    elif room_area in range(151, 251):
        btu = 6000
    elif room_area in range(251, 301):
        btu = 7000
    elif room_area in range(301, 351):
        btu = 8000
    elif room_area in range(351, 401):
        btu = 9000
    elif room_area in range(401, 451):
        btu = 10000
    elif room_area in range(451, 551):
        btu = 12000
    elif room_area in range(551, 701):
        btu = 14000
    else:
        btu = btu_calc_2(room_area)
    return btu


def btu_calc_2(room_area):
    """Room -> BTU"""
    if room_area in range(701, 1001):
        btu = 18000
    elif room_area in range(1001, 1201):
        btu = 21000
    elif room_area in range(1201, 1401):
        btu = 23000
    elif room_area in range(1401, 1501):
        btu = 24000
    elif room_area in range(1501, 2001):
        btu = 30000
    elif room_area in range(2001, 2501):
        btu = 34000
    return btu


def air_btu():
    """BTU"""
    room_area = int(input())
    room_height = int(input())
    population = int(input())
    special = str(input())
    position = str(input())
    btu = btu_calc(room_area) + (1000 * max(room_height - 8, 0)) + \
        (600 * max(population - 2, 0)) + (4000 * (special == "kitchen"))
    if position == "facing the sun":
        btu += btu * 0.1
    elif position == "shaded":
        btu -= btu * 0.1
    print(int(btu))


air_btu()
