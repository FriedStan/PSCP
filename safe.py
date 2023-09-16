"""Safe"""


def crack_the_safe(safe_key, current_lock):
    """Open the safe by use the lowest move"""
    alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    move_make = 0
    for i, char in enumerate(safe_key):
        lock_move = abs(alphabeth.find(current_lock[i]) - alphabeth.find(char))
        move_make += min(lock_move, abs(26 - lock_move))
    print(move_make)


crack_the_safe(str(input()), str(input()))
