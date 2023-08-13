"""Nearer"""


def nearest_pos(alice_pos, bob_pos, icetruck_pos):
    """Who is nearer?"""
    alice_distance = abs(alice_pos - icetruck_pos)
    bob_distance = abs(bob_pos - icetruck_pos)
    if alice_distance > bob_distance:
        who_get = "Bob " + str(bob_distance)
    elif alice_distance < bob_distance:
        who_get = "Alice " + str(alice_distance)
    else:
        who_get = "Sundaes " + str(min(alice_distance, bob_distance))
    return who_get


print(nearest_pos(int(input()), int(input()), int(input())))
