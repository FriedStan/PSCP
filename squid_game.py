"""Octopus game"""


def team_force():
    """Get pull force from team"""
    force = 0
    for _ in range(10):
        force += int(input())
    return force


def show_begin():
    """Let's the tug begin"""
    a_force = team_force()
    b_force = team_force()
    print("A" * (a_force <= b_force) + "B" * (a_force >= b_force))


show_begin()
