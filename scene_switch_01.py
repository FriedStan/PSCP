"""SceneSwitch I"""


def swicher_morelike_swiching(action_time):
    """https://youtu.be/9EDZixuODrw?si=XNV2pqyxKA_2w7nL"""
    prev_time = action_time
    light = ["Closed", "Daylight", "Warmwhite"]
    state = light[1]
    prev_state = light[1]
    count = 0
    while action_time != "End":
        if state != light[0] and action_time != "0":
            state = light[0]
        elif float(action_time) - float(prev_time) > 6 and state == light[0]:
            state = light[1]
            prev_state = light[1]
        elif prev_state != light[1] and action_time != "0":
            state = light[1]
            prev_state = state
        elif prev_state != light[2] and action_time != "0":
            state = light[2]
            count += 1
            prev_state = state
        prev_time = action_time
        action_time = str(input())
    print(count)


swicher_morelike_swiching(str(input()))
