"""Brick Bridge"""


def bridge_maker(goal, brick_a, brick_b):
    """Make big Bridge"""
    need_b = goal // 5
    if need_b <= brick_b:
        usage_b = need_b
    else:
        usage_b = brick_b
    usage_a = goal - (usage_b * 5)
    if (usage_b * 5) + usage_a == goal and usage_a <= brick_a:
        result = usage_a
    else:
        result = -1
    return result


def main():
    """Main func"""
    brick_a = int(input())
    brick_b = int(input())
    goal = int(input())
    print(bridge_maker(goal, brick_a, brick_b))


main()
