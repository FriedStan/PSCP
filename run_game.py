"""RunGame"""


def run_game_online(target_pos):
    """Run Forest Run"""
    prev_pos = 0
    ran_distance = 0
    for target in target_pos:
        ran_distance += abs(prev_pos - target)
        prev_pos = target
    print(ran_distance)


run_game_online(map(int, str(input()).split()))
