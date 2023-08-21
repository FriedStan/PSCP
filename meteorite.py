"""[Midterm 2022] Meteorite"""


def meteor_strike(size, split_into, not_a_threat):
    """Calculate missile for strike the meteor"""
    missile = 0
    current_meteor = 1
    while size >= not_a_threat:
        missile += 1 * current_meteor
        just_shoot = 1 * current_meteor
        size /= split_into
        current_meteor = split_into * just_shoot
    return missile


print(meteor_strike(float(input()), int(input()), float(input())))
