"""ATM"""


def automatic_teller_machine(action):
    """ATM"""
    default = int(action)
    while action != ["END"]:
        action = str(input()).split()
        if len(action) != 1:
            default += int(action[1]) if action[0] == "D" else -1 * int(action[1])
            default = max(0, default)
    print(default)


automatic_teller_machine(str(input()).upper())
